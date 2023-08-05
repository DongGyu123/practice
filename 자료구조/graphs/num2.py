def dfs_recursion(G, v):
  visited=[False]*n
  visited[v] = True
  visit(v)  # do something useful
  for w in G[v]:  # G[v] returns the neighbors of v
    if not visited[w]:
      dfs_recursion(G, w)

def dfs_iteration(stack, v):
  visited = []
  stack = [v]
  while stack:
    v = stack.pop()
    if v not in visited:
      visited.append(v)
      visit(v)
      stack.extend(G[v] - set(visited))


def valid_path(n, edges, source, destination):
  '''
  >>> n = 6
  >>> edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
  >>> source = 0
  >>> destination = 5
  >>> valid_path(n, edges, source, destination)
  False
  >>> n = 3
  >>> edges = [[0,1],[1,2],[2,0]]
  >>> source = 0
  >>> destination = 2
  >>> valid_path(n, edges, source, destination)
  True
  '''
  # solution 1. DFS
  adjacency_list = [[] for _ in range(n)]
  
  for a, b in edges:
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)
  
  stack = [source]
  visited = set()  # visited = [ False ] * n
  
  while stack:
    # Get the current node.
    node = stack.pop()
    
    # Check if we have reached the target node.
    if node == destination:
      return True
    
    # Check if we've already visited this node.
    if node in visited:
      continue
    
    visited.add(node)
    
    # Add all neighbors to the stack.
    for neighbor in adjacency_list[node]:
      stack.append(neighbor)
  
  # Our stack is empty and we did not reach the destination node.
  return False
