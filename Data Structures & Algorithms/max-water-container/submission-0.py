class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxArea=0
        left,right=0,len(h)-1
        while left<right:
            currArea = (right-left)*min(h[right], h[left])
            maxArea=max(currArea, maxArea)
            if h[right]>=h[left]:
                left+=1
            else:
                right-=1
        return maxArea