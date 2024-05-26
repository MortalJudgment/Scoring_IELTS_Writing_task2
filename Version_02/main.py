
from textwrap import dedent
from crewai import Crew, Process


from tasks import Tasks
from agents import Agents

# Collect input from the user
question = "in many countries, governments are interesting in new technology to deal with the public. Why is this happening? Do you think this is an appropriate use of government money?"
essay = """In today's modern age, there is a tendency for many governments all over the world to use new technological methods in order to address the community rather than approach the public in a conventional way due to the increasing demand for use effectively. With the convenience of time and the sustainability of investment, I totally contend that technology in terms of politics is a potential development which should be invested.

Initially, the reason why governments in many countries choose  technology as a primary way to solve social problems is that this way saves time a lot. In other words, it is an evolution in fostering other critical problems by using saved time without regarding too much on the only issues in society. To explain, if the governments receive taxes from people, even poor ones but do not tackle problems such as crime crises or alarming others well enough, they will be criticized seriously by residents, however, if they complete their role, they will get the belief from people. Thus, the technology put them ahead by the timing value.

Another point worth considering is the stable investment in technology. Spending money on technological advantage is a good way to either save money or approach different communities easily in a nation. For instance, technology allows the government to identify individuals more easily, moreover, in order to save money, the government have to invest just only expense on technological things but brings a lot of worthy benefits of funding for governments as well as provides the efficiency of catching up with new information for human. Hence, the practical benefits of money spent on technology can give a new opportunity for government in particular and nation in general in order to enhance evolutionary innovation in terms of mechanism.

Taking all points into account, one cannot deny the advantageous elements of  time and stable investment. Investing money in technology is not only away to approach the public but also publicize the revolution of the modern world.
"""

# Create Agents
agents = Agents()

scoring_IELTS_agent = agents.IELTS_Writing_agent()
scoring_CC_agent = agents.Coherence_and_Cohesion_agent()
scoring_LR_agent = agents.Lexical_Resource_agent()
scoring_GR_agent = agents.Grammatical_Range_and_Accuracy_agent()
scoring_TR_agent = agents.Task_Response_agent()

# Task
tasks = Tasks()
scoring_IELTS_task = tasks.scoring_IELTS(question, essay, scoring_IELTS_agent)
scoring_CC_task = tasks.scoring_CC_task(question, essay, scoring_CC_agent)
scoring_LR_task = tasks.scoring_LR_task(question, essay, scoring_LR_agent)
scoring_GR_task = tasks.scoring_GR_task(question, essay, scoring_GR_agent)
scoring_TR_task = tasks.scoring_TR_task(question, essay, scoring_TR_agent)
# Assemble Crew
crew = Crew(
    agents=[scoring_IELTS_agent, scoring_CC_agent, scoring_LR_agent, scoring_GR_agent, scoring_TR_agent],
    tasks=[scoring_IELTS_task, scoring_CC_task,  scoring_LR_task, scoring_GR_task, scoring_TR_task],
    verbose=True,
    # process=Process.sequential
)

# Kickoff the crew to perform tasks
scoring = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(scoring)