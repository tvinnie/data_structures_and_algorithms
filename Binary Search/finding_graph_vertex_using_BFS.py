"""
## INSTRUNCTIONS:

Check if you found the search value.
Return True if you found the search value.
Inside the for loop, check if the adjacent vertex has been visited.
Return False if you didn't find the search value.

"""

import queue

def bfs(graph, initial_vertex, search_value):
  visited_vertices = []
  bfs_queue = queue.SimpleQueue()
  visited_vertices.append(initial_vertex)
  bfs_queue.put(initial_vertex)

  while not bfs_queue.empty():
    current_vertex = bfs_queue.get()
    # Check if you found the search value
    if current_vertex == search_value:
      # Return True if you find the search value
      return True    
    for adjacent_vertex in graph[current_vertex]:
      # Check if the adjacent vertex has been visited
      if adjacent_vertex not in visited_vertices:
        visited_vertices.append(adjacent_vertex)
        bfs_queue.put(adjacent_vertex)
  # Return False if you didn't find the search value
  return False

print(bfs(graph, '4', '8'))

## OUTPUT:
"""
True

"""