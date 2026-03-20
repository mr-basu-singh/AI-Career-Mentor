from langchain_tavily import TavilySearch

def get_tavily_tool():
    return TavilySearch(k=3)