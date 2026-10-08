class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultDict automatically assigns a default value 
        # to keys that do not exist.
        adj = defaultdict(list)
        # sort the tickets lexicographically then reverse???
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        # itinerary
        res = []

        # dfg
        def dfs(src):
            # consume all edges
            while adj[src]:
                # remove the last item in the (reversed) adjacency list 
                # (earliest lexicographically)
                dst = adj[src].pop()
                # recurse
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]