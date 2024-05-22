import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import SequentialChain
from langchain.prompts.prompt import PromptTemplate
#from langchain_core.prompts import PromptTemplate
from langchain_contrib.prompts import ChainedPromptTemplate
from langchain import LLMChain
from langgraph.checkpoint.sqlite import SqliteSaver

#from getpass import getpass

#export API_KEY="AIzaSyAvMS1PkJBBYql65I_IE_RHeqbjjG0Z7YU"
#api_key = getpass()
api_key= os.environ['API_KEY']

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
#content = llm.invoke( "What are some of the pros and cons of Python as a programming language?")

st.title("Chatbot App for Writing IELTS task 2")

# Define the individual steps as prompt templates
identify_type_prompt = PromptTemplate(
    input_variables=["essay_prompt"],
    template="""
    Identify the type of essay prompt. Is it Argumentative/Opinion, Discussion, Advantages and Disadvantages, Causes and Effects/Solutions, or Two-Part Question?
    Essay Prompt: {essay_prompt}
    """
)

evaluate_task_response_prompt = PromptTemplate(
    input_variables=["essay"],
    template="""
    Evaluate the Task Response based on the essay type. Does the essay address all parts of the question appropriately? Is the response clear and relevant?
    Essay: {essay}
    """
)

evaluate_coherence_cohesion_prompt = PromptTemplate(
    input_variables=["essay"],
    template="""
    Evaluate Coherence and Cohesion. Are the ideas logically organized and well-connected? Are cohesive devices used effectively?
    Essay: {essay}
    """
)

evaluate_lexical_resource_prompt = PromptTemplate(
    input_variables=["essay"],
    template="""
    Evaluate the Lexical Resource. Is there a good range of vocabulary used appropriately? Are there instances of precise and varied word choice?
    Essay: {essay}
    """
)

evaluate_grammatical_range_accuracy_prompt = PromptTemplate(
    input_variables=["essay"],
    template="""
    Evaluate Grammatical Range and Accuracy. Is there a variety of grammatical structures used correctly? Are there errors that impact understanding?
    Essay: {essay}
    """
)

overall_band_score_prompt = PromptTemplate(
    input_variables=["task_response_score", "coherence_cohesion_score", "lexical_resource_score", "grammatical_range_accuracy_score"],
    template="""
    Consider the individual scores for each criterion. How do these contribute to the overall quality of the essay?
    Task Response Score: {task_response_score}
    Coherence and Cohesion Score: {coherence_cohesion_score}
    Lexical Resource Score: {lexical_resource_score}
    Grammatical Range and Accuracy Score: {grammatical_range_accuracy_score}
    """
)

# Combine the prompts into a sequence (chain)
evaluation_chain = ChainedPromptTemplate(
    steps=[
        identify_type_prompt,
        evaluate_task_response_prompt,
        evaluate_coherence_cohesion_prompt,
        evaluate_lexical_resource_prompt,
        evaluate_grammatical_range_accuracy_prompt,
        overall_band_score_prompt
    ],
    joiner="\n\n"
)

# Define input essay and prompt
essay_prompt = "Some people think that environmental problems should be solved on a global scale while others believe it is better to deal with them nationally. Discuss both sides and give your opinion."
student_essay = """
In recent years, environmental issues have become a major concern for many countries. While some argue that these problems should be addressed on a global level, others believe that national governments should take responsibility. This essay will discuss both perspectives and provide my opinion.

On one hand, addressing environmental issues globally can lead to more comprehensive solutions. Many environmental problems, such as climate change and pollution, are not confined to national borders. Therefore, international cooperation is essential to effectively tackle these issues. Global agreements, such as the Paris Agreement, are examples of how countries can work together to reduce greenhouse gas emissions and combat climate change.

On the other hand, national governments have a crucial role to play in solving environmental problems. Each country has its unique environmental challenges, and national policies can be tailored to address these specific issues. Additionally, national governments can implement regulations and policies more quickly and efficiently than international bodies. For example, a country can enforce stricter emissions standards for industries within its borders, which can have an immediate impact on reducing pollution.

In my opinion, both global and national approaches are necessary to effectively address environmental problems. While international cooperation provides a framework for tackling global issues, national governments can take concrete actions to address local environmental challenges. Therefore, a combined approach that leverages the strengths of both global and national efforts is the most effective way to protect our environment.
"""

# Execute the evaluation chain
results = evaluation_chain.run({
    "essay_prompt": essay_prompt,
    "essay": student_essay
})

# Print the results
for step, result in zip(evaluation_chain.steps, results):
    content = f"{step.input_variables}: {result}"
    st.markdown(content)

st.success("Complete!")