class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        checker = {i :[] for i in range(n)}
        if len(edges) > n - 1:
            return False
        for s, e in edges:
            checker[s].append(e)
            checker[e].append(s)
        #check for obeying edges rule
        
        visit = set()

        def dfs(n, prev):
            if n in visit:
                return False

            visit.add(n)

            for nq in checker[n]:
                if nq == prev:
                    continue

                if not dfs(nq, n):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)



        
        