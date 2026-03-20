import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.graph.workflow import build_graph


def run_graph():
    graph = build_graph()

    user_query = input("Enter your query: ")

    # ✅ Intent Handling
    if user_query.lower() in ["hi", "hello", "hey"]:
        print("\n👋 Hello! I am your AI Career Mentor.")
        print("Ask me about any career (AI, CA, Law, Business, etc.)")
        return

    if len(user_query.split()) < 3:
        print("\n⚠️ Please enter a clear career goal.")
        print("Example: 'I want to become Data Scientist'")
        return

    result = graph.invoke({
        "user_query": user_query
    })

    print("\n===== FINAL OUTPUT =====\n")
    print(result["final_output"])