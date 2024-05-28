import streamlit as st
import time
from Version_03 import model as md
from data import getdata


# Model name
C_MODEL = "mixtral-8x7b-32768"
A_MODEL = "llama3-70b-8192"
B_MODEL = "llama3-8b-8192"

# Path to your JSON file
simon_file = getdata.load_simon()

# Choose a random key from the list
# if 'random_key_1' not in st.session_state:
#     keys = list(simon_file.keys())
#     st.session_state['random_key_1']  = random.choice(keys)
st.session_state['random_key_1'] = "5"
random_key = st.session_state['random_key_1'] 
random_item = simon_file[random_key]
essay_question = random_item['question']
#essay_answer = random_item['text']['answer'].replace("\r\n", "\r\n\r\n")
essay_answer = random_item['answer']
essay_type = random_item['questionType']


def score_criteria(criteria, question, essay):
    validate_response = md.Validate_calling(question, essay, criteria, model_name=C_MODEL )
    score_response = md.Detail_Score(question, essay, criteria, model_name=A_MODEL, previous_results=validate_response)
    feedback_response = md.Give_feedback(score_response, essay, criteria, model_name=A_MODEL)
    final_response = md.Refine_results_to_final_output(score_response, feedback_response, criteria, model_name=B_MODEL)

    return final_response

def create_agent(criteria,name):
    if st.session_state[f'button_{name}'] == False:
        with st.spinner('Processing...'):
            time.sleep(3)

        start_time = time.time()
        # while True:
        #     BOSS_command = md.manager(essay_question, essay_answer, model_name = B_MODEL, previous_task = process)
        #     process.append(BOSS_command.strip('\'"'))
        #     if "Complete" in process:
        #         break
        #     else:
        #         validate_response = md.Validate_calling(essay_question, essay_answer, criteria = BOSS_command, model_name=C_MODEL)
        #         score_response = md.Detail_Score(essay_question, essay_answer, criteria = BOSS_command , model_name=A_MODEL, previous_results=validate_response)
        #         feedback_response = md.Give_feedback(score_response, essay_answer, criteria  = BOSS_command , model_name=A_MODEL)
        #         final_response = md.Refine_results_to_final_output(score_response, feedback_response, criteria = BOSS_command, model_name=B_MODEL)
        response = score_criteria(criteria, essay_question,essay_answer)
        end_time = time.time()
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)
        execution_time = end_time - start_time

        st.session_state[f'button_{name}'] = True

        yield f"Execution time: {execution_time:.2f} seconds. \r\n\r\n {response}" 

def clear():
    for key in st.session_state.keys():
        del st.session_state[key]


# ---- Sidebar ---

st.sidebar.markdown("# IELST Examiner Simon Score:")
st.sidebar.markdown(f"## Overband: {random_item['band']}")
# st.sidebar.divider()
# st.sidebar.markdown(f"## Task Achievement: {random_item['results']['bands']['taBand']}")
# if 'gpt' in random_item['results'].keys():
#     st.sidebar.markdown(f"- Complete Response: {random_item['results']['gpt']['scores']['task_achievement']['complete_response']}")
#     st.sidebar.markdown(f"- Clear Comprehensive Ideas: {random_item['results']['gpt']['scores']['task_achievement']['clear_comprehensive_ideas']}")
#     st.sidebar.markdown(f"- Relevant Specific Examples: {random_item['results']['gpt']['scores']['task_achievement']['relevant_specific_examples']}")
# st.sidebar.markdown(f"- Answer Question: {random_item['results']['sections']['answerQuestion']}")
# st.sidebar.markdown(f"- Idea Explanation: {random_item['results']['sections']['ideaExplanation']}")
# st.sidebar.markdown(f"- Include Conclusion: {random_item['results']['sections']['includeConclusion']}")
# st.sidebar.markdown(f"- Include Examples: {random_item['results']['sections']['includeExamples']}")
# st.sidebar.divider()
# st.sidebar.markdown(f"## Coherence Cohesion: {random_item['results']['bands']['coherenceBand']}")
# if 'gpt' in random_item['results'].keys():
#     st.sidebar.markdown(f"- Logical Structure: {random_item['results']['gpt']['scores']['coherence_cohesion']['logical_structure']}")
#     st.sidebar.markdown(f"- Introduction Conclusion Present: {random_item['results']['gpt']['scores']['coherence_cohesion']['introduction_conclusion_present']}")
#     st.sidebar.markdown(f"- Supported Main Points: {random_item['results']['gpt']['scores']['coherence_cohesion']['supported_main_points']}")
# st.sidebar.markdown(f"- Linking Words Count: {random_item['results']['sections']['linkingWordsCount']}")
# st.sidebar.markdown(f"- Linking Words Density: {random_item['results']['sections']['linkingWordsDensity']}")
# st.sidebar.markdown(f"- Paragraph Structure: {random_item['results']['sections']['paragraphsStructure']}")
# st.sidebar.divider()
# st.sidebar.markdown(f"## Lexical: {random_item['results']['bands']['lexicalBand']}")
# st.sidebar.markdown(f"- Vocabulary: {random_item['results']['sections']['vocabulary']}")
# st.sidebar.markdown(f"## Grammar: {random_item['results']['bands']['grammaticBand']}")
# st.sidebar.markdown(f"- Grammar GPT: {random_item['results']['sections']['grammar']}")



#--- Main ---
with st.container():
    if essay_type != '':
        st.write(f"<span style='color:333'>#{random_item['questionType']}</span>",unsafe_allow_html=True)
    st.header(essay_question)
    with st.expander("Essay Answer:"):
        st.write(essay_answer,unsafe_allow_html=True)

    # Define tab information
    criterias = {
        "ta" : "Task Response",
        "cc" : "Coherence and Cohesion", 
        "lx" : "Lexical Resource", 
        "gm" : "Grammatical Range and Accuracy", 
    }

    # Create tabs
    tabs = st.tabs(criterias.values())

    # Initialize session state
    for name in criterias.keys():
        if f'button_{name}' not in st.session_state:
            st.session_state[f'button_{name}'] = False

    # Loop through tabs and dynamically generate content
    for tab, criteria, name in zip(tabs, criterias.values(), criterias.keys() ):
        with tab:
            if st.button(f'Scoring {criteria}' ):
                st.write_stream(create_agent(criteria,name))

    # With magic:
    #st.session_state
    st.button('Clear', on_click=clear)
            
