class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = set()
        for n in nums:
            if n in hashed:
                return True
            hashed.add(n)
        return False