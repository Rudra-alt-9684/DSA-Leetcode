class Solution:
    def pivotIndex(self, n: list[int]) -> int:
        t = sum(n)
        l = 0

        for i in range(len(n)):
            r = t - l - n[i]

            if l == r:
                return i
            
            l += n[i]
        
        return -1

