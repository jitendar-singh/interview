from queue import Queue

adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D","F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
}

visited, parent,  level,  queue, bfs_traversal_output = {}, {}, {}, Queue(), []

for node in adj_list.keys():
    visited[node] = False
    parent[node] =  None
    level[node] = -1

s = "A"
queue.put(s)
visited[s] = True
level[s] = 0

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
            
print(bfs_traversal_output)

print(level)

n, path = "G", list()
print("Type of path:", type(path))
print("Type of n:", type(n))
while n is not None:
    path.append(n)
    n = parent[n]
path.reverse()
print(path)