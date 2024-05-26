import sys
import os
import time
from rich.console import Console
from rich.panel import Panel
from groq import Groq
from prompt import ValidatePrompt, ScoringPrompt, RefinedOutput

from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

console = Console()
validate_prompt = ValidatePrompt()
scoring_prompt = ScoringPrompt()
output_refined = RefinedOutput()

client = Groq(api_key=groq_api_key)

C_MODEL = "mixtral-8x7b-32768"
A_MODEL = "llama3-70b-8192"
B_MODEL = "llama3-8b-8192"

def manager(question, essay, model_name, previous_task):
    if previous_task == []:
        previous_task = "Let's start!"
        console.print("\n[bold yellow]Let's start Evaluating IELTS Writing task 2[/bold yellow]")

    system_prompt = """You are the manager of a group of AI Agents tasked with evaluating IELTS Writing Task 2.
                    The team needs to evaluate based on 4 criteria: 
                    - "Coherence and Cohesion"
                    - "Lexical Resource"
                    - "Grammatical Range and Accuracy"
                    - "Task Response"

                    Your job is to let the team know which criteria they should evaluate next to complete the task.
                    If the task has just begun, return the first criteria: "Coherence and Cohesion".
                    If all criteria have been evaluated as indicated in the user prompt, return "Complete".
                    You MUST NOT return a criterion that has already been done.
                    Your return should be a single criterion or "Complete" at a time (do not give other words or information).
                    """ 
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Here are the criteria have been evaluated as indicated:\n {previous_task}.\n\n If all the criteria is done then return 'Complete'. Otherwise, return next criteria"},
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=1000,
    )

    response_text = response.choices[0].message.content

    return response_text


def Validate_calling(question, essay, criteria, model_name):
    if "Coherence and Cohesion" in criteria:
        band_description = validate_prompt.Coherence_and_Cohesion()
    elif "Lexical Resource" in criteria:
        band_description = validate_prompt.Lexical_Resource()
    elif "Grammatical Range and Accuracy" in criteria:
        band_description = validate_prompt.Grammatical_Range_and_Accuracy()
    elif "Task Response" in criteria:
        band_description = validate_prompt.Task_Response()
    else:
        sys.exit("ERROR on Criteria name")

    console.print("\n[bold yellow]Validating the score using Band descriptions[/bold yellow]")

    system_message = "You are an AI assistant using the IELTS band descriptors to validate the score of the essay. Be wise, careful, and honest in your evaluation."

    messages = [
        {"role": "system", "content": system_message},
        {
            "role": "user",
            "content": f"""Given IELTS writing task 2 question: '{question}' 
            Essay: '{essay}' 
            Given the Band Descriptions below, what score would you give to the above essay on the {criteria} criteria?
            {band_description}
            """
        },
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=8000,
    )

    response_text = response.choices[0].message.content
    
    console.print(
        Panel(
            response_text,
            title="[bold blue]Validation-agent Result[/bold blue]",
            title_align="left",
            border_style="blue",
            subtitle="Completed validation, sending result to next step 👇",
        )
    )
    return response_text

def Detail_Score(question, essay, criteria, model_name, previous_results):
    console.print("\n[bold blue]Detail Score[/bold blue]")

    if "Coherence and Cohesion" in criteria:
        prompt = scoring_prompt.Coherence_and_Cohesion()
    elif "Lexical Resource" in criteria:
        prompt = scoring_prompt.Lexical_Resource()
    elif "Grammatical Range and Accuracy" in criteria:
        prompt = scoring_prompt.Grammatical_Range_and_Accuracy()
    elif "Task Response" in criteria:
        prompt = scoring_prompt.Task_Response()
    else:
        sys.exit("ERROR on Criteria name")


    messages = [
        {
            "role": "system",
            "content": f"You are an AI assistant that evaluates the {criteria} criteria of an IELTS Writing Task 2 essay. Provide previous results, think step by step, and give reasoning on sub-criteria. List strong points, weak points. What factors contribute to a high score in this category, and how would you identify them in an essay? Note that the lowest sub-criteria score MUST equal the overall {criteria} score."
        },
        {
            "role": "user",
            "content": f"""Given an IELTS writing Task 2
            Question: '{question}'
            Essay: '{essay}'
            And the previous validated score using Band descriptions: {previous_results}.
            Give a detailed score on sub-criteria. NOTE THAT!!! The sub-criteria score MUST be an integer and NOT LOWER than the overall {criteria} score.
            {prompt}
            """
        }
    ]


    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=8000,
    )

    response_text = response.choices[0].message.content

    console.print(
        Panel(
            response_text,
            title=f"[bold green]Scoring {criteria} using {model_name} [/bold green]",
            title_align="left",
            border_style="green",
            subtitle="Completed detailed scoring, sending result to next step 👇",
        )
    )

    return response_text

def Give_feedback(previous_results, essay, criteria, model_name):
    console.print("\n[bold magenta]Generating feedback[/bold magenta]")

    messages = [
        {
            "role": "system",
            "content": f"You are an AI assistant providing detailed feedback and improvement on an IELTS {criteria} criteria to get a better result."
        },
        {
            "role": "user",
            "content": f"""Here are the scoring results:
            {previous_results}
            Then give improvement on its sub-criteria.
            Provide constructive general feedback (about 100 words).
            """
        }
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=8000,
    )

    feedback_text = response.choices[0].message.content
    console.print(
        Panel(
            feedback_text,
            title="[bold purple]Feedback[/bold purple]",
            title_align="left",
            border_style="purple",
            subtitle="Feedback generated, sending to final refinement 👇",
        )
    )
    return feedback_text

def Refine_results_to_final_output(score_response, feedback, criteria, model_name=B_MODEL):
    console.print("\n[bold cyan]Refining final output[/bold cyan]")


    if "Coherence and Cohesion" in criteria:
        prompt = output_refined.Coherence_and_Cohesion()
    elif "Lexical Resource" in criteria:
        prompt = output_refined.Lexical_Resource()
    elif "Grammatical Range and Accuracy" in criteria:
        prompt = output_refined.Grammatical_Range_and_Accuracy()
    elif "Task Response" in criteria:
        prompt = output_refined.Task_Response()
    else:
        sys.exit("ERROR on Criteria name")

    messages = [
        {
            "role": "system",
        "content": "You are an AI assistant compiling a comprehensive report for an IELTS Writing Task 2 essay. You will be given an output from a {criteria} criteria evaluation, and I need it translated and rewritten in a natural and friendly tone for a Vietnamese user. Keep the criteria and sub-criteria in English, but translate the rest."
        },
        {
            "role": "user",
            "content": f"Given {score_response}\n\n{feedback}\n\n{prompt}"
        }
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=8000,
    )

    final_report = response.choices[0].message.content
    console.print(
        Panel(
            final_report,
            title="[bold blue]Final Report[/bold blue]",
            title_align="left",
            border_style="blue",
        )
    )
    return final_report

question = "The increase in the production of consumer goods results in damage to the natural environment. What are the causes of this? What can be done to solve this problem?"
essay = """Nowadays, as more consumer goods are manufactured, more damage has been inflicted on the environment. I will outline several reasons for this and put forward some measures to this issue.

First of all, the increase in the production of consumer products harms the environment in two ways: the chemical by-products from the manufacturing process and the mass production of disposable goods. As more goods are produced, more toxic wastes and emissions are released from factories into nature. Water sources are contaminated, and the air is severely polluted, which results in the deaths of many marine and terrestrial animals. Also, to accommodate customers’ ever-increasing demands, more single-use products are introduced, most of which are non-biodegradable. Though having a short lifespan, these products can remain as wastes for thousands of years, turning our planet into a huge landfill and posing a threat to the living habitats of all creatures.

Actions must be taken as soon as possible to minimize the negative impacts on the environment arising from the increasing amount of consumer goods. First, companies should promote the use of eco-friendlier materials. For example, the giant coffee chain Starbucks has recently replaced plastic straws with reusable alternatives made of materials like paper or bamboo. In addition, many governments are also encouraging the development of more sustainable manufacturing processes. For instance, many states in the U.S offer tax breaks and incentives for businesses using renewable energy, and some firms are even allowed to purchase green energy at cheaper prices than traditional fossil fuels.

In conclusion, there are two main reasons why the environment is severely impacted by the increase in the production of consumer goods. To address this issue, governments and companies must join hands to make the production lines more environmentally friendly by switching to greener materials."""

criterias = ["Coherence and Cohesion", "Lexical Resource", "Grammatical Range and Accuracy", "Task Response"]

process = []
start_time = time.time()
while True:
    BOSS_command = manager(question, essay, model_name = B_MODEL, previous_task = process)
    process.append(BOSS_command.strip('\'"'))
    if "Complete" in process:
        break
    else:
        validate_response = Validate_calling(question, essay, criteria = BOSS_command, model_name=C_MODEL)
        score_response = Detail_Score(question, essay, criteria = BOSS_command , model_name=A_MODEL, previous_results=validate_response)
        feedback_response = Give_feedback(score_response, essay, criteria  = BOSS_command , model_name=A_MODEL)
        final_response = Refine_results_to_final_output(score_response, feedback_response, criteria = BOSS_command, model_name=B_MODEL)
end_time = time.time() - start_time
print(end_time)
