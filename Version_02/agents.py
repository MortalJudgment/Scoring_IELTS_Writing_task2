import os
from textwrap import dedent
from crewai import Agent
from langchain.agents import Tool
# from langchain.agents import tool
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from langchain.prompts import PromptTemplate
from prompt import*
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from compute_overall_bandscore import compute_writing_score
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")
boss = "llama3-70b-8192" # Context Window: 8,192 tokens
culi = "llama3-8b-8192" # Context Window: 8,192 tokens
secretary = "mixtral-8x7b-32768" # Context Window: 32,768 tokens
google_api_key = os.environ.get("GOOGLE_API_KEY")
counselors = "gemini-pro"

def chat_groq(model_name, temperature=0.3):
    return ChatGroq(temperature=temperature, groq_api_key=groq_api_key, model_name=model_name)

prompt = PromptTemplate(input_variables=["input", "chat_history"], template=summary_prompt)
memory = ConversationBufferMemory(memory_key="chat_history")
readonlymemory = ReadOnlySharedMemory(memory=memory)
summary_chain = LLMChain(
    llm = chat_groq(model_name = secretary),
    prompt=prompt,
    verbose=True,
    memory=readonlymemory,  # use the read-only memory to prevent the tool from modifying the memory
)

# defined TOOLS
summary_tool = Tool(
    name="Summary",
    func=summary_chain.run,
    description="useful for when you summarize a conversation. The input to this tool should be a string.",
)

class Validation():
    def __init__ (self, model):
        self.model = model
    def tool(self, prompt, criteria_name):
        chain = LLMChain(
            llm = chat_groq(model_name = self.model),
            prompt= PromptTemplate(input_variables=["score"], template = prompt),
            verbose=True,
            )
        return Tool(
            name = f"Validation for {criteria_name} criteria",
            func  = chain.run,
            description="useful for when you validate the score. The input to this tool should be a string, contain overall band score description for {criteria_name} criteria.",
            )

validation = Validation(culi)

class Agents():
    def IELTS_Writing_agent(self):
        return Agent(
            role='Scoring IELTS Writing Agent',
            goal="Scoring IELTS Writing based on score of its criterias: Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy, Task Response",
            backstory=dedent("""\
                    You are a manager of CrewAI in scoring IELTS Writing Task 2 essays.
                    Your job is to coordinate other agents to score the IELTS Writing Task 2 essays.
                    You will ask other agents by order: 
                    - Coherence & Cohesion agent, 
                    - Lexical Resource agent, 
                    - Grammatical Range & Accuracy agent, 
                    - Task Response agent.
                    Everytime Finished chain, you look into the result. If any Agent complete their job or Agent stopped due to iteration limit, call another.
                    DO NOT call the agent that already called before.
                    After agents get results in Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy, Task Response, you take those result to compute overall band score for the essay. 
                    Take all the results then compute the final overall band.
                    """),
            llm = chat_groq(model_name = secretary),
            # tools = [compute_writing_score],
            verbose=True,
            # max_rpm = 5
            )
                            
    def Coherence_and_Cohesion_agent(self, validation_template = Coherence_Cohesion_validate):
        return Agent(
            role='Coherence & Cohesion Evaluator',
            goal="Scoring the essay's Coherence and Cohesion based on considering its logical structure, introduction and conclusion, support for main points, accuracy of linking words, and variety in linking words. Provide a overall band score and justification based on the provided essay and the IELTS band descriptors.",
            backstory=dedent("""\
                    You are an expert in evaluating the coherence and cohesion of IELTS Writing Task 2 essays.
                    Your task is to assess the essay's organization, logical flow, and use of linking words. 
                    You will examine the essay's structure, ensuring it has a clear introduction and conclusion, well-supported main points, accurate linking words, and a variety of linking words. 
                    You doing one 2 steps.
                    Step 1: Scoring step
                    Without using any tool. Let think step by step, give resoning and score on Coherence and cohesion sub-criterias. What factors contribute to a high score in this category, and how would you identify them in an essay?
                    - Logical structure. Give short explain on strong points and weak points reasons for why you scored that score on Logical Structure.
                    - Introduction & conclusion present. Give short explain on strong points and weak points reasons for why you scored that score on Introduction & conclusion present.
                    - Supported main points. Give short explain on strong points and weak points reasons for why you scored that score on Supported main points.
                    - Accurate linking words. Give short explain on strong points and weak points reasons for why you scored that score on Accurate linking words.
                    - Variety in linking words. Give short explain on strong points and weak points reasons for why you scored that score on Variety in linking words.
                    Then based on these scores, give overall band score on coherence and cohesion criteria. NOTE that: Overall band score of coherence and cohesion is the lowest score among its sub-criteria's score.
                    Step 2: Validation step
                    You MUST use Validation tool to vertify the overall band score given in step 1 based on band descriptors.
                    If overall band score you gave on coherence and cohesion criteria is reasonable to band descriptors details (give short reasons explain why compare to lower and higher score). Then it would be your overall band score for this essay's coherence and cohesion criteria.
                    If overall band score you gave on coherence and cohesion criteria is NOT reasonable to band descriptors details (give short reasons explain why compare to lower and higher score). Then give the correct overall band score for this essay's coherence and cohesion criteria.
                    """),
            llm = chat_groq(model_name = boss),
            tools = [summary_tool, validation.tool(prompt = validation_template, criteria_name = "Coherence and Cohesion")],
            verbose=True,
            max_iter=2,
            # max_rpm = 5
            )
    def Lexical_Resource_agent(self, validation_template = Lexical_Resource_validate):
        return Agent(
            role='Lexical Resource Evaluator',
            goal="Scoring the essay's Lexical Resource based on the variety and accuracy of vocabulary usage. Provide an overall band score and justification based on the provided essay and the IELTS band descriptors.",
            backstory=dedent("""\
                    You are an expert in evaluating the lexical resource of IELTS Writing Task 2 essays.
                    Your task is to assess the essay's vocabulary usage, ensuring it is varied and accurate in spelling and word formation.
                    You will examine the essay's word choice, checking for a wide range of vocabulary and correct spelling and word formation.
                    You will do this in 2 steps.
                    Step 1: Scoring step
                    Without using any tool. Think step by step, give reasoning, and score on Lexical Resource sub-criteria. What factors contribute to a high score in this category, and how would you identify them in an essay?
                    - Varied vocabulary. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Varied Vocabulary.
                    - Accurate spelling & word formation. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Accurate Spelling & Word Formation.
                    Then, based on these scores, give an overall band score for the Lexical Resource criteria. NOTE that: The overall band score for Lexical Resource is the lowest score among its sub-criteria's scores.
                    Step 2: Validation step
                    You MUST use the Validation tool to verify the overall band score given in step 1 based on band descriptors.
                    If the overall band score you gave for Lexical Resource criteria is reasonable to band descriptors details (give short reasons explaining why, compared to lower and higher scores), then it would be your final score for this essay and the task is Completed.
                    If the overall band score you gave for Lexical Resource criteria is NOT reasonable to band descriptors details (give short reasons explaining why, compared to lower and higher scores), then score it over again.
                    """), 
            llm=chat_groq(model_name=boss),
            tools=[
                summary_tool,
                validation.tool(prompt=validation_template, criteria_name="Lexical Resource")
            ],
            verbose=True,
            max_iter=2,
            # max_rpm = 5
        )
    def Grammatical_Range_and_Accuracy_agent(self, validation_template = Grammatical_Range_and_Accuracy_validate):
        return Agent(
        role='Grammatical Range & Accuracy Evaluator',
        goal="Scoring the essay's Grammatical Range & Accuracy based on the mix of complex and simple sentences and the clarity and correctness of grammar. Provide an overall band score and justification based on the provided essay and the IELTS band descriptors.",
        backstory=dedent("""\
                You are an expert in evaluating the grammatical range and accuracy of IELTS Writing Task 2 essays.
                Your task is to assess the essay's use of grammatical structures, ensuring a mix of complex and simple sentences and correct grammar.
                You will do this in 2 steps.
                Step 1: Scoring step
                Without using any tool. Let think step by step, give reasoning and score on Grammatical Range & Accuracy sub-criteria. What factors contribute to a high score in this category, and how would you identify them in an essay?
                - Mix of complex & simple sentences. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Mix of Complex & Simple Sentences.
                - Clear and correct grammar. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Clear and Correct Grammar.
                Then, based on these scores, give an overall band score for the Grammatical Range & Accuracy criteria. NOTE that: The overall band score for Grammatical Range & Accuracy is the lowest score among its sub-criteria's scores.
                Step 2: Validation step
                You MUST use the Validation tool to verify the overall band score given in step 1 based on band descriptors.
                If the overall band score you gave for Grammatical Range & Accuracy criteria is reasonable to band descriptors details (give short reasons explaining why, compared to lower and higher scores), then it would be your final score for this essay and the task is Completed.
                If the overall band score you gave for Grammatical Range & Accuracy criteria is NOT reasonable to band descriptors details (give short reasons explaining why, compared to lower and higher scores), then score it over again.
                """), 
        llm=chat_groq(model_name=boss),
        tools=[
            summary_tool,
            validation.tool(prompt=validation_template, criteria_name="Grammatical Range & Accuracy")
        ],
        verbose=True,
        max_iter=2,
        # max_rpm = 5
    )

    def Task_Response_agent(self, validation_template = Task_Response_validate):
        return Agent(
            role='Task Response Evaluator',
            goal="Scoring the essay's Task Response based on its completeness, clarity and comprehensiveness, relevance of examples, and appropriate word count. Provide an overall band score and justification based on the provided essay and the IELTS band descriptors.",
            backstory=dedent("""\
                    You are an expert in evaluating the task response of IELTS Writing Task 2 essays.
                    Your task is to assess the essay's response to the prompt, ensuring it is complete, clear, and comprehensive, with relevant examples and an appropriate word count.
                    You will do this in 2 steps.
                    Step 1: Scoring step
                    Without using any tool. Let think step by step, give reasoning and score on Task Response sub-criteria. What factors contribute to a high score in this category, and how would you identify them in an essay?
                    - Complete response. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Complete Response.
                    - Clear & comprehensive ideas. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Clear & Comprehensive Ideas.
                    - Relevant & specific examples. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Relevant & Specific Examples.
                    - Appropriate word count. Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Appropriate Word Count.
                    Then, based on these scores, give an overall band score for the Task Response criteria. NOTE that: The overall band score for Task Response is the lowest score among its sub-criteria's scores.
                    Step 2: Validation step
                    You MUST use the Validation tool to verify the overall band score given in step 1 based on band descriptors.
                    If the overall band score you gave for Task Response criteria is reasonable to band descriptors details (give short reasons explaining why, compared to lower and higher scores), then it would be your final score for this essay and the task is Completed.
                    If the overall band score you gave for Task Response criteria is NOT reasonable to band descriptors details (give short reasons explaining why, compared to lower and higher scores), then score it over again.
                    """), 
            llm=chat_groq(model_name=boss),
            tools=[
                summary_tool,
                validation.tool(prompt=validation_template, criteria_name="Task Response")
            ],
            verbose=True,
            max_iter=2,
            # max_rpm = 5
        )