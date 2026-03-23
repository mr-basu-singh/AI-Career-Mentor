from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def final_agent(user_query, plan, research):
    formatted_research = ""

    if isinstance(research, list):
        for item in research:
            formatted_research += f"\n- {item.get('title')}: {item.get('content')[:150]}...\n"

    prompt = f"""
You are a smart career advisor for students in India.

User Query:
{user_query}

Career Plan:
{plan}

Market Research:
{formatted_research}

Give:
- Personalized career advice
- Practical steps
- Industry-relevant suggestions
- Avoid generic answers
"""

    response = llm.invoke(prompt)

    return f"""
📊 Final Output

{plan}

🔥 Market Insights:
{formatted_research}

💡 Smart Advice:
{response.content}
"""