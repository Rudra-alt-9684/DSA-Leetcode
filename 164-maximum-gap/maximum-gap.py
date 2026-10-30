class Solution:
    def maximumGap(self, n: list[int]) -> int:
        if len(n) < 2:
            return 0

        n = sorted(n)
        m = 0
        s = 0

        for i in range(len(n)-1):
            s = n[i+1] - n[i]
            m = max(m, s)
            
        return m 

        