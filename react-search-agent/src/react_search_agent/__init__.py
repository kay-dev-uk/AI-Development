from typing import List

from pydantic import BaseModel, Field
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

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the response from the agent"""

    answer:str = Field(description="The agent's answer to the query")
    source: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm = ChatOpenAI(model="gpt-5.2-2025-12-11")
# tools = [search]
tools= [TavilySearch()]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main() -> None:
    print("Hello from react-search-agent!")
    result = agent.invoke(
            {
            "messages": HumanMessage(
                content="I'm in market for Washing Dryer in the UK. I'm looking for the best options available. I need a reliable machine, from a reliable brand with reputation, decent warranty and least amount of customer complaints. My budget is £600 (including discounts). I want you to find options online and provide them. Don't give more than 5 options. It needs to wash at least 8kgs and dry at least 5kgs. It needs to be efficient (But if it's not too reliable but super effieicent that is a bad option) and super reliable. It needs to be relatively new in terms of release date. Good to have a beltless motor but not necessary. Any little brands or non reliable brands - please ignore. I wash and dry quite regurarly so it's a key thing for me. You are free to provide cheaper options as long as they match the criteria. Obviously include AppliancesDirect, Currys and Argos in your search but not limit to it."
                )
            }
        )
    print(result)

main()