#dijkstra algorithm

import heapq
def dj(v, edges, src):
    adjList=[]
    for i in range(v):
        adjList.append([])
    for n, m, w in edges:
        adjList[n].append((m, w))
        adjList[m].append((n, w))
    distance=[float("inf")]*v
    pq=[]
    distance[src]=0
    heapq.heappush(pq, (0, src))
    while(pq):
        dist, node=heapq.heappop(pq)
        for adjNode, adjDist in adjList[node]:
            if(dist+adjNode<distance[adjNode]):
                distance[adjNode]=dist+adjDist
                heapq.heappush(pq, (dist+adjDist, adjNode))
    return distance
v=3
edges=[[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src=0
print(dj(v, edges, src))