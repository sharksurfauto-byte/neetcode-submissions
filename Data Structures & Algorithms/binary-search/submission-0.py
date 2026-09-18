class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        st, end = 0, n-1
        while st<=end:
            mid = int(st + (end-st)/2)
            if nums[mid]==target:
                return mid
            
            elif nums[mid]>target:
                end = mid-1
            else:
                st = mid+1
        
        return -1