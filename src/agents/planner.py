from src.llm.llm_groq import get_llm

def planner_agent(user_query):
    llm = get_llm()

    prompt = f"""
    You are a career planning expert.

    Break the following goal into step-by-step learning roadmap:

    Goal: {user_query}

    Give structured steps.
    """

    response = llm.invoke(prompt)
    return response.content