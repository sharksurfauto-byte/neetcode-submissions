class Solution:
    def isalphanum(self, c:str):
        return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if not self.isalphanum(s[l]):
                l+=1
            elif not self.isalphanum(s[r]):
                r-=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l+=1
                r-=1
        return True
