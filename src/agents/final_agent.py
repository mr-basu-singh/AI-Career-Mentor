from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def final_agent(user_query, plan, research):
    formatted_research = ""

    if isinstance(research, list):
        for item in research:
            formatted_research += f"\n- {item.get('title')}: {item.get('content')[:150]}...\n"

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a smart career advisor for Indian students."),
        ("human", """
User Query: {user_query}

Career Plan:
{plan}

Market Research:
{research}

Give:
1. Personalized Smart Advice
2. Industry Insights
3. Final Suggestion

Keep it simple and practical.
""")
    ])

    chain = prompt | llm

    response = chain.invoke({
        "user_query": user_query,
        "plan": plan,
        "research": formatted_research
    })

    return f"""
📊 Final Output

{plan}

🔥 Market Insights:
{formatted_research}

💡 Smart Advice:
{response.content}
"""