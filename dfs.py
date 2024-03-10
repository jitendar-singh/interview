adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}

color = {} # W, G, B
parent = {}
trav_time = {} #[start, end]
dfs_trav_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] =  None
    trav_time[node] = [-1, -1]

time = 0

def dfs_utils(u):
    global time
    color[u] = "G"
    dfs_trav_output.append(u)
    trav_time[u][0] = time
    time+=1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_utils(v)
    color[u] = "B"
    trav_time[u][1] = time
    time+=1

dfs_utils("A")
print(dfs_trav_output)
for node in adj_list.keys():
    print(node, '->',trav_time[node])