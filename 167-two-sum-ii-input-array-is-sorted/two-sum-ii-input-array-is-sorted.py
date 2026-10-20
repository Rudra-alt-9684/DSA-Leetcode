class Solution:
    def twoSum(self, n: list[int], t: int) -> list[int]:
        l = 0
        r = len(n)-1
        sum = 0
        
        while l < r:
            sum = n[l] + n[r]
            if sum == t:
                return [l+1,r+1]
            elif sum > t:
                r = r-1
            else:
                l = l+1 
        