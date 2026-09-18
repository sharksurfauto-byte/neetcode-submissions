class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)
        for c,p in prerequisites:
            graph[c].append(p)
        
        state = [0]*numCourses

        def dfs(course):
            # base case
            if state[course]==1:
                return False
            if state[course]==2:
                return True
            
            state[course]=1

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            state[course]=2
            order.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order