def bfs(i, visited, q, adj, ans):
    while(q):
        node=q.pop(0)
        for it in adj[node]:
            if(visited[it]==0):
                visited[it]=1
                q.append(it)
        ans.append(it)
def bf(adj):
    ans=[]
    v=len(adj)
    visited=[0]*v
    for i in range(0, v):
        if(visited[i]==0):
            visited[i]=1
            q=[i]
            bfs(i, visited, q, adj, ans)
    return ans
adj=[[1,2], [0,3,4], [0,5,6], [1], [1], [2], [2]]
print(bf(adj))