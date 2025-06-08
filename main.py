from graph import graph


if __name__=="__main__":
    state = {"messages": [{"role": "user", "content": "Who won the euro 2024"}], "max_research_loops": 3, "initial_search_query_count": 3}
    # output = graph.invoke(state)
    # print(output.keys())
    # print(output)
    for chunk in graph.stream(state):
        print(chunk)
    # print()
    # generate_query({
    # "messages": [{"role": "human", "content": "AI"}], 
    # "max_research_loops": 3, 
    # "initial_search_query_count": 3
    # })
#     query_list = {"query_list":['"current state of machine learning research" 2025',
#   '"ethical implications of AI development" 2025',
#   '"future trends in machine learning applications" 2025']}
# continue_to_web_research(query_list)
