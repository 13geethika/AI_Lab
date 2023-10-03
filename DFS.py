from collections import defaultdict
graph={}
n=int(input("enter no.of nodes "))
for i in range(0,n):
    a=input()
    neighs=[]
    b='1'
    while(b!='0'):
        b=input()
        if b!='0':
            neighs.append(b)
    graph[a]=neighs
def dfs(visited, graph, node):  
    if node not in visited:
        print (node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print(" Depth-First Search order is ")
visited = []
dfs(visited, graph, '5')