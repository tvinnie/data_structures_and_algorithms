"""
## INSTUCTIONS:

Check if current_vertex hasn't been visited yet.
Add current_vertex to visited_vertices.
Call dfs() recursively by passing it the appropriate values.

"""
def dfs(visited_vertices, graph, current_vertex):
    # Check if current_vertex hasn't been visited yet
    if current_vertex not in visited_vertices:
        print(current_vertex)
        # Add current_vertex to visited_vertices
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            # Call recursively with the appropriate values
            dfs(visited_vertices, graph, adjacent_vertex)
            
dfs(set(), graph, '0')

## OUTPUT
"""
0
1
2
4
3

"""