import streamlit as st
import os
import time
from graph import graph  # Replace with actual file name if it's not named this

st.set_page_config(page_title="LangGraph Tracker", layout="centered")
st.title("🔍 LangGraph Execution Viewer")

# Input box for user query
user_query = st.text_input("🧠 Ask a question:", "Who won the euro 2024?")
max_loops = st.slider("🔁 Max Research Loops", min_value=1, max_value=5, value=3)
initial_queries = st.slider("🔍 Initial Search Queries", min_value=1, max_value=5, value=3)

run_button = st.button("🚀 Run Agent")

if run_button:
    st.info("Running LangGraph agent... Please wait ⏳")
    placeholder = st.empty()
    timeline = []

    # Prepare state
    state = {
        "messages": [{"role": "user", "content": user_query}],
        "max_research_loops": max_loops,
        "initial_search_query_count": initial_queries,
    }

    # Stream from LangGraph
    for chunk in graph.stream(state):
        node = list(chunk.keys())[0]
        data = chunk[node]
        timeline.append((node, data))

        # Live update display
        with placeholder.container():
            st.subheader("📍 LangGraph Execution Timeline")
            for step_idx, (n, d) in enumerate(timeline):
                with st.expander(f"{step_idx+1}. {n}", expanded=False):
                    st.json(d)
    st.write(data["messages"][-1].content)

    st.success("✅ Finished processing!")
