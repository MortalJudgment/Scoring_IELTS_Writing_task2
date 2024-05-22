import streamlit as st
import os
from run_groq import Groq

# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

from action1 import get_score
from action2 import get_score_with_feedback
from action3 import suggest_outline

load_dotenv()

# groq_api_key = "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"
groq_api_key = os.environ.get("GROQ_API_KEY")

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
    question = st.text_input("Enter your question:")
    essay = st.text_area("Enter your essay:")
    
    if st.button("Submit"):
        all_response = []
        for index, (key, value) in enumerate(criteria.items()):
            with st.spinner(f"Scoring {key} criteria..."):
                response = get_score(question, essay, chat, key, value)
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
        st.markdown(overall)
        st.success("Complete!")
    
def option2(chat):
    question = st.text_input("Enter your question:")
    essay = st.text_area("Enter your essay:")
    
    if st.button("Submit"):
        for index, (key, value) in enumerate(criteria.items()):
            with st.spinner(f"Scoring {key} criteria..."):
                response = get_score_with_feedback(question, essay, chat, key, value)
                st.markdown(response)
        
        st.success("Complete!")
        # Process the inputs and do something
    
def option3(chat):
    question = st.text_input("Enter your question:")

    # Create a place for users to input a number using a slider
    selected_number = st.slider("Select desired score:", min_value = 6.0, max_value = 9.0, step = 0.5)

    # Display the selected number
    if st.button("Submit"):
        with st.spinner("Please wait ..."):
            response = suggest_outline(chat, question, selected_number)
            st.markdown(response)
        st.success("Believe you can and you're halfway there!")

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