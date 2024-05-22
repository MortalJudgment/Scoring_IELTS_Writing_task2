from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from crewai import Agent, Crew, Process, Task
from crewai_tools import tool
from langchain.agents import load_tools
from langchain_community.tools import DuckDuckGoSearchResults
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(temperature=0, model_name="llama3-70b-8192")


system = "You are experienced Machine Learning & AI Engineer."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

parser = StrOutputParser()

chain = prompt | model | parser
response = chain.invoke({"text": "How to write a React promt to evaluate writing ielts task 2?"})

#-- Tools --#
search_tool = DuckDuckGoSearchResults(backend="news", num_results=10)

@tool("search tool")
def cryptocurrency_news_tool(ticker_symbol: str) -> str:
     """Get news for a given cryptocurrency ticker symbol"""
     return search_tool.run(ticker_symbol + " cryptocurrency")

human_tools = load_tools(["human"])
#-- Agent --#
customer_communicator = Agent(
    role="Senior cryptocurrency customer communicator",
    goal="Find which cryptocurrency the customer is interested in",
    backstory="""You're highly experienced in communicating about cryptocurrencies
    and blockchain technology with customers and their research needs""",
    verbose=True,
    allow_delegation=False,
    llm=model,
    max_iter=5,
    memory=True,
    tools=human_tools,
)
news_analyst = Agent(
    role="Cryptocurrency News Analyst",
    goal="""Get news for a given cryptocurrency. Write 1 paragraph analysis of
    the market and make prediction - up, down or neutral.""",
    backstory="""You're an expert analyst of trends based on cryptocurrency news.
    You have a complete understanding of macroeconomic factors, but you specialize
    into analyzing news.
    """,
    verbose=True,
    allow_delegation=False,
    llm=model,
    max_iter=5,
    memory=True,
    tools=[cryptocurrency_news_tool],
)
#-- Tasks --#
get_cryptocurrency = Task(
    description=f"Ask which cryptocurrency the customer is interested in.",
    expected_output="""Cryptocurrency symbol that the human wants you to research e.g. BTC.""",
    agent=customer_communicator,
)
get_news_analysis = Task(
    description=f"""
    Use the search tool to get news for the cryptocurrency

    Compose the results into a helpful report""",
    expected_output="""Create 1 paragraph report for the cryptocurrency,
    along with a prediction for the future trend
    """,
    agent=news_analyst,
    context=[get_cryptocurrency],
)
#-- Crew --#
crew = Crew(
    agents=[customer_communicator, news_analyst],
    tasks=[get_cryptocurrency, get_news_analysis],
    verbose=2,
    process=Process.sequential,
    full_output=True,
    share_crew=False,
    manager_llm=model,
    max_iter=15,
)

results = crew.kickoff()