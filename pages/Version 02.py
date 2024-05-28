
from textwrap import dedent
from crewai import Crew
from Version_02 import tasks
from Version_02 import agents
from data import getdata
import streamlit as st
import time

# Collect input from the user
# question = "in many countries, governments are interesting in new technology to deal with the public. Why is this happening? Do you think this is an appropriate use of government money?"
# essay = """In today's modern age, there is a tendency for many governments all over the world to use new technological methods in order to address the community rather than approach the public in a conventional way due to the increasing demand for use effectively. With the convenience of time and the sustainability of investment, I totally contend that technology in terms of politics is a potential development which should be invested.

# Initially, the reason why governments in many countries choose  technology as a primary way to solve social problems is that this way saves time a lot. In other words, it is an evolution in fostering other critical problems by using saved time without regarding too much on the only issues in society. To explain, if the governments receive taxes from people, even poor ones but do not tackle problems such as crime crises or alarming others well enough, they will be criticized seriously by residents, however, if they complete their role, they will get the belief from people. Thus, the technology put them ahead by the timing value.

# Another point worth considering is the stable investment in technology. Spending money on technological advantage is a good way to either save money or approach different communities easily in a nation. For instance, technology allows the government to identify individuals more easily, moreover, in order to save money, the government have to invest just only expense on technological things but brings a lot of worthy benefits of funding for governments as well as provides the efficiency of catching up with new information for human. Hence, the practical benefits of money spent on technology can give a new opportunity for government in particular and nation in general in order to enhance evolutionary innovation in terms of mechanism.

# Taking all points into account, one cannot deny the advantageous elements of  time and stable investment. Investing money in technology is not only away to approach the public but also publicize the revolution of the modern world.
# """

ielts = getdata.load_writing9()

# Choose a random key from the list
if 'random_key_4' not in st.session_state:
    st.session_state['random_key_4']  = getdata.load_random(ielts)
    
random_key = st.session_state['random_key_4'] 
random_item = ielts['data'][random_key]
question = random_item['text']['question']
essay = random_item['text']['answer'].replace("\r\n", "\r\n\r\n")

def run_agent():
    # Create Agents
    ag = agents.Agents()

    scoring_IELTS_agent = ag.IELTS_Writing_agent()
    scoring_CC_agent = ag.Coherence_and_Cohesion_agent()
    scoring_LR_agent = ag.Lexical_Resource_agent()
    scoring_GR_agent = ag.Grammatical_Range_and_Accuracy_agent()
    scoring_TR_agent = ag.Task_Response_agent()

    # Task
    ta = tasks.Tasks()
    scoring_IELTS_task = ta.scoring_IELTS(question, essay, scoring_IELTS_agent)
    scoring_CC_task = ta.scoring_CC_task(question, essay, scoring_CC_agent)
    scoring_LR_task = ta.scoring_LR_task(question, essay, scoring_LR_agent)
    scoring_GR_task = ta.scoring_GR_task(question, essay, scoring_GR_agent)
    scoring_TR_task = ta.scoring_TR_task(question, essay, scoring_TR_agent)
    # Assemble Crew
    crew = Crew(
        agents=[scoring_IELTS_agent, scoring_CC_agent, scoring_LR_agent, scoring_GR_agent, scoring_TR_agent],
        tasks=[scoring_IELTS_task, scoring_CC_task,  scoring_LR_task, scoring_GR_task, scoring_TR_task],
        verbose=True,
        # process=Process.sequential
    )

    # Kickoff the crew to perform tasks
    start_time = time.time()
    scoring = crew.kickoff()
    end_time = time.time()
    complete_time = end_time - start_time
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
    yield f"Execution time: {complete_time:.2f} seconds."
    time.sleep(0.2)

    # Print results
    yield scoring
    time.sleep(0.2)


#-- Main --#
st.header(question)

with st.expander("Essay Answer:"):
    st.write(essay,unsafe_allow_html=True)

if st.button("Run CrewAI"):
    st.write_stream(run_agent())