from src.tools.tavily_tool import get_tavily_tool

def researcher_agent(query):
    tool = get_tavily_tool()
    
    result = tool.invoke({"query": query})
    
    # Extract useful info
    final_results = []
    
    for item in result.get("results", [])[:3]:
        title = item.get("title")
        url = item.get("url")
        content = item.get("content")
        
        formatted = f"""
Title: {title}
URL: {url}
Summary: {content}
"""
        final_results.append(formatted)
    
    return "\n\n".join(final_results)