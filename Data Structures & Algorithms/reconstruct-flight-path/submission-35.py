class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.e = self.makeQueue(tickets)
        currentKey = "JFK"
        self.pathLength = len(tickets) + 1
        visited = []


        # Hecking Concurrent Modification Bug
        """
                def dfs(currentKey):
            for edge in self.e[currentKey]:
                    self.e[currentKey].remove(edge)
                    dfs(edge)
            visited.append(currentKey)
        """
        
        def dfs(currentKey):
            while self.e.get(currentKey):
                    edge = self.e[currentKey].pop(0)
                    dfs(edge)
            visited.append(currentKey)

        dfs(currentKey)
        return visited[::-1]
                    


    def useTicket(self, currentKey, edge):
        self.e[currentKey].remove(edge)


    def makeQueue(self, tickets):
        e = defaultdict(list)
        for src, dst in sorted(tickets):
            e[src].append(dst)
        return e