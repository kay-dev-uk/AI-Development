from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import AIMessage, HumanMessage, content
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch


# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5.2-2025-12-11")
# tools = [search]
tools= [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from react-search-agent!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job posting for a Outsystems developer 3+ years of experience, in the UK, preferably remote, exclude any listings with many applicants or the ones that aren't recent. Show salary, date posted and brief requirements. exclude Paragon or Pluxee.")})
    print(result)

main()