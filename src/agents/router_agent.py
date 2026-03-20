from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

def router_agent(user_query):
    prompt = f"""
You are an intent classifier.

Classify the input into ONLY one of these:
- greeting
- career query
- other

Rules:
- "hi", "hello", "hey" → greeting
- anything about job/career → career query
- unclear/random → other

Input: {user_query}

Output ONLY one word from above.
"""

    response = llm.invoke(prompt)

    # ✅ Clean + Normalize Output
    intent = response.content.strip().lower()

    # ✅ Safety Mapping (VERY IMPORTANT)
    if "greet" in intent:
        return "greeting"
    elif "career" in intent:
        return "career query"
    else:
        return "other"