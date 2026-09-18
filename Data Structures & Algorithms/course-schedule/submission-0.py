from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)   
        for c,p in prerequisites:
            graph[c].append(p)
        
        state = [0]*numCourses

        def dfs(course):
            if state[course]==1:
                return False
            
            if state[course]==2:
                return True
            
            state[course]=1
            for nei in graph[course]:
                if not dfs(nei):
                    return False

            state[course]=2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True