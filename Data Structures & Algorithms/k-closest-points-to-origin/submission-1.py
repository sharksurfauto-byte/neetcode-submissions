import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return x**2 + y**2
        
        min_heap = []

        for x,y in points:
            d = distance(x,y)
            heapq.heappush(min_heap, (-d,x,y))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
            
        return [(x,y) for _,x,y in min_heap]
        
        