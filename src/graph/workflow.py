from langgraph.graph import StateGraph
from typing import TypedDict

from src.agents.planner import planner_agent
from src.agents.researcher import researcher_agent
from src.agents.final_agent import final_agent


# Define state
class GraphState(TypedDict):
    user_query: str
    plan: str
    research: str
    final_output: str


# Nodes
def planner_node(state):
    plan = planner_agent(state["user_query"])
    return {"plan": plan}


def research_node(state):
    research = researcher_agent(state["user_query"])
    return {"research": research}

def final_node(state):
    final = final_agent(
        state["user_query"], 
        state["plan"], 
        state["research"]
    )
    return {"final_output": final}

# Build graph
def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("planner", planner_node)
    builder.add_node("research", research_node)
    builder.add_node("final", final_node)   # ✅ NEW NODE

    # Flow
    builder.set_entry_point("planner")
    builder.add_edge("planner", "research")
    builder.add_edge("research", "final")   # ✅ CONNECT TO FINAL

    builder.set_finish_point("final")       # ✅ FINAL OUTPUT HERE

    return builder.compile()