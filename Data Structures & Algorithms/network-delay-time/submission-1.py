class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.times = times
        distances = [float('inf')] * (n+1)
        distances[k] = 0
        visited = [False] * (n+1)

        for _ in range(n):
            minDistance = float('inf')
            u = None
            for i in range(1, n+1):
                # If we haven't visited this node and it's a finite distance away:
                if not visited[i] and distances[i] < minDistance:
                    minDistance = distances[i]
                    u = i
            
            # We are done.
            if u is None:
                break

            visited[u] = True
            for v in range(1, n+1):
                edge = self.getEdge(u, v)
                if edge is not None and minDistance + edge < distances[v]:
                    distances[v] = minDistance + edge
            
        
        if max(distances[1:]) == float('inf'):
            return -1
        return max(distances[1:])


    def getEdge(self, u, v):
        for time in self.times:
            if time[0] == u and time[1] == v:
                return time[2]
        