class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connectedComponents = 0
        visited = [False] * n 
        adj = self.makeAdjList(edges)
        V = list(range(n)) 


        def dfs(cur):
            visited[cur] = True
            for u in adj.get(cur, []):
                if not visited[u]:
                    dfs(u)
        
        for v in V:
            if not visited[v]:
                connectedComponents += 1
                dfs(v)
        return connectedComponents


    def makeAdjList(self, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj 