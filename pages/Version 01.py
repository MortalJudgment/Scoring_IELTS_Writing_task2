import streamlit as st
import time
import os
from groq import Groq
import json 
import random

from dotenv import load_dotenv

from Version_01 import action1 
from Version_01 import action2 
from Version_01 import action3 

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")

# Path to your JSON file
filename = "./data/writing9.json"

# Open the file in read mode
with open(filename, "r") as f:
  # Load the data from the file
  ielts = json.load(f)

# Choose a random key from the list

if 'question_1' not in st.session_state:
    st.session_state['question_1'] = ''
if 'essay_1' not in st.session_state:
    st.session_state['essay_1'] = ''
if 'band_1' not in st.session_state:
    st.session_state['band_1'] = ''

# Define the function to autoload samples
def autoload_samples():
    #if 'random_key_2' not in st.session_state:
    keys = list(ielts['data'].keys())
    st.session_state['random_key_2']  = random.choice(keys)
    random_key = st.session_state['random_key_2'] 
    random_item = ielts['data'][random_key]
    question_sample = random_item['text']['question']
    essay_sample = random_item['text']['answer'].replace("\r\n", "\r\n\r\n")
    band_sample = random_item['text']['band']
    st.session_state['question_1'] = question_sample
    st.session_state['essay_1'] = essay_sample
    st.session_state['band_1'] = band_sample

if groq_api_key is None:
    st.error("GROQ API key not found in environment variables.")
    st.stop()  

criteria = {
    'Coherence and cohesion': ['Logical structure', 'Introduction & conclusion present', 'Supported main points', 'Accurate linking words', 'Variety in linking words'], 
    'Lexical Resource': ['Varied vocabulary', 'Accurate spelling & word formation'], 
    'Grammatical Range': ['Mix of complex & simple sentences', 'Clear and correct grammar'], 
    'Task Achievement': ['Complete response', 'Clear & comprehensive ideas', 'Relevant & specific examples', 'Appropriate word count (yes or no)']
    }


def option1(chat):
    question = st.text_input("Enter your question:", value=st.session_state['question_1'])
    essay = st.text_area("Enter your essay:", value=st.session_state['essay_1'])

    if st.button("Autoload Essay", on_click=autoload_samples):
        st.write(f"Sample data band {st.session_state['band_1']} (reference) loaded.")
    
    if st.button("Submit"):
        all_response = []
        start_time = time.time()
        for index, (key, value) in enumerate(criteria.items()):
            with st.spinner(f"Scoring {key} criteria..."):
                response = action1.get_score(question, essay, chat, key, value)
                all_response.append(response)
                # st.markdown(response)
        overall = chat(f"""Instruction: For OVERALL BAND SCORE, it is computed by the average of 4 criterias: Coherence and cohesion, Lexical Resource, Grammatical Range, Task Achievement. And rounded up (.5). \n
                        For example: Coherence and cohesion: 6, Lexical Resource: 6, Grammatical Range: 5, Task Achievement: 6. OVERALL BAND SCORE would be compute by (6 + 6 + 5 + 6)/4 = 5.75 and rounded up to 6.0. 
                        Therefore, OVERALL BAND SCORE: 6.0.\n 
                        Now based on {all_response}, compute OVERALL BAND SCORE (do not give reason to this, give final OVERALL BAND SCORE ONLY)
                        Please provide a structured breakdown of your assessment results, including scores for each criterion as follows (fill score ONLY to ...):
                        Coherence and Cohesion: ...
                        - Logical structure: ...
                        - Introduction & conclusion present: ...
                        - Supported main points: ...
                        - Accurate linking words: ...
                        - Variety in linking words: ...

                        Lexical Resource: ...
                        - Varied vocabulary: ...
                        - Accurate spelling & word formation: ...

                        Grammatical Range: ...
                        - Mix of complex & simple sentences: ...
                        - Clear and correct grammar: ...

                        Task Achievement: ...
                        - Complete response: ...
                        - Clear & comprehensive ideas: ...
                        - Relevant & specific examples: ...
                        - Appropriate word count:

                        OVERALL BAND SCORE: ...""") 
        end_time = time.time()
        complete_time = end_time - start_time
        st.markdown(overall)
        st.success(f"Complete! Executive time is {complete_time}")

    
def option2(chat):
    question = st.text_input("Enter your question:", value=st.session_state['question_1'])
    essay = st.text_area("Enter your essay:", value=st.session_state['essay_1'])

    if st.button("Autoload Essay", on_click=autoload_samples):
        st.write(f"Sample data band {st.session_state['band_1']} (reference) loaded.")
    
    if st.button("Submit"):
        start_time = time.time()
        for index, (key, value) in enumerate(criteria.items()):
            with st.spinner(f"Scoring {key} criteria..."):
                response = action2.get_score_with_feedback(question, essay, chat, key, value)
                st.markdown(response)
        end_time = time.time()
        complete_time = end_time - start_time
        st.success(f"Complete! Executive time is {complete_time}")
        # Process the inputs and do something
    
def option3(chat):
    question = st.text_input("Enter your question:", value=st.session_state['question_1'] )

    if st.button("Autoload Essay", on_click=autoload_samples):
        st.write(f"Question loaded.")

    # Create a place for users to input a number using a slider
    selected_number = st.slider("Select desired score:", min_value = 6.0, max_value = 9.0, step = 0.5)

    # Display the selected number
    if st.button("Submit"):
        start_time_3 = time.time() 
        with st.spinner("Please wait ..."):
            response = action3.suggest_outline(chat, question, selected_number)
            st.markdown(response)
        end_time_3 = time.time() 
        complete_time = end_time_3 - start_time_3
        st.success(f"Executive time is {complete_time}")

def main():

    st.title("Chatbot App for Writing IELTS task 2")

    # Add customization options to the sidebar
    st.sidebar.title('Select an LLM')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama3-70b-8192', 'llama3-8b-8192', 'gemma-7b-it', 'mixtral-8x7b-32768']
    )
    st.sidebar.title('Select a Task')
    option = st.sidebar.selectbox("Select an option:", ["Scoring", "Give feedback and improvement", "Give an instruction"])

    def chat_groq(prompt, temperature=0):
        client = Groq(
            api_key = groq_api_key,
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model = model,
            temperature = temperature,
        )

        return chat_completion.choices[0].message.content

    if option == "Scoring":
        option1(chat = chat_groq)
    elif option == "Give feedback and improvement":
        option2(chat = chat_groq)
    elif option == "Give an instruction":
        option3(chat = chat_groq)

if __name__ == "__main__":
    main()