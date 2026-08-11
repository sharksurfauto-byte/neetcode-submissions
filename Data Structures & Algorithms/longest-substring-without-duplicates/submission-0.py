class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        lastSeen={}
        maxWindow=0
        for right in range(len(s)):
            if s[right] in lastSeen:
                left = max(left, lastSeen[s[right]]+1)
            lastSeen[s[right]]=right
            maxWindow=max(maxWindow, right-left+1)
        return maxWindow