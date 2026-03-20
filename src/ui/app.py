import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.graph.workflow import build_graph
from src.agents.router_agent import router_agent

st.set_page_config(page_title="AI Career Mentor", layout="centered")

st.title("🤖 AI Career Mentor (Multi-Agent System)")

user_query = st.text_input("Enter your career goal:")


if st.button("Generate Roadmap"):
    if user_query:

        intent = router_agent(user_query)

        # ✅ DEBUG LINE
        st.write(f"DEBUG → Intent: {intent}")

        if intent == "greeting":
            st.write("👋 Hello! I am your AI Career Mentor.")

        elif intent == "career query":
            graph = build_graph()

            with st.spinner("Thinking..."):
                result = graph.invoke({"user_query": user_query})

            st.subheader("📊 Final Output")
            st.write(result["final_output"])

        else:
            st.warning("⚠️ Please ask a clear career-related question.")