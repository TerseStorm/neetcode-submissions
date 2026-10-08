class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.e = self.makeQueue(tickets)
        currentKey = "JFK"
        self.pathLength = len(tickets) + 1
        visited = []


        def dfs(currentKey):
            while self.e[currentKey]:
                    edge = self.e[currentKey].pop(0)
                    dfs(edge)
            visited.append(currentKey)

        dfs(currentKey)
        return visited[::-1]
                    


    def useTicket(self, currentKey, edge):
        self.e[currentKey].remove(edge)


    def makeQueue(self, tickets):
        # defaultDict automatically assigns a default value 
        # to keys that do not exist.
        adj = defaultdict(list)
        # sort the tickets lexicographically then reverse???
        for src, dst in sorted(tickets):
            adj[src].append(dst)
        return adj