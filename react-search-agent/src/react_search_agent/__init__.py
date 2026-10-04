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
                content="Tell me the weather in NYC briefly"
                )
            }
        )
    print(result)

main()