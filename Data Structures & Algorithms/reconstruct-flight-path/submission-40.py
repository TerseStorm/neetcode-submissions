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

        """
        In Python, .pop(0) on a standard list is an $O(N)$ operation. Because it removes the first item, Python has to shift every single remaining item in memory one step to the left. If a node has a massive list of outbound edges, this becomes a bottleneck.
        """
        
        def dfs(currentKey):
            while self.e.get(currentKey):
                    edge = self.e[currentKey].pop()
                    dfs(edge)
            visited.append(currentKey)

        dfs(currentKey)
        return visited[::-1]
                    


    def makeQueue(self, tickets):
        e = defaultdict(list)
        # List reversal is done because pop is O(1) from the end of the list (I guess.)
        for src, dst in sorted(tickets)[::-1]:
            e[src].append(dst)
        return e