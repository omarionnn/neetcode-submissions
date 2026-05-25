class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for n in adj_list[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n 




            


        
        