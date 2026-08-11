class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # [73,74,75,71,69,72,76,73]
        n=len(temps)
        ans=[0]*n
        stack=[]
        for i in range(n):
            if stack:
                while stack and temps[i]>temps[stack[-1]]:
                    idx=stack.pop()
                    ans[idx]=i-idx
            stack.append(i)
        return ans