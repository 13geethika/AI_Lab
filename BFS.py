graph = {'5':['3','7','9'],'3':['2', '4','14'],'7':['8'],'2':[],'4':['8'],'8':[],'9':['5','10'],'14':[],'10':[]}
visited = [] 
queue = []     
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  while queue:        
    m = queue.pop(0) 
    print (m, end = " ") 
    for adj in graph[m]:
        if adj not in visited:
            visited.append(adj)
            queue.append(adj)
print("Breadth-First Search order is ")
bfs(visited, graph, '5')    