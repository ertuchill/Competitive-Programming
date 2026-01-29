#Algoleague-Topological Sort

import heapq

n, e = map(int, input().split())
dag = [[] for i in range(n+1)]
indegree = [0] * (n+1)

for _ in range(e):
    u,v = map(int, input().split())
    dag[v].append(u)
    indegree[u] += 1

pq=[]
result=[]
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while len(pq)!=0:
    current = heapq.heappop(pq)
    result.append(current)
    for adj in dag[current]:
        indegree[adj]-=1
        if indegree[adj]==0:
            heapq.heappush(pq,adj)
            
print(result)