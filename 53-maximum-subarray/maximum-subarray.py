class Solution:
    def maxSubArray(self, n: list[int]) -> int:
        c = n[0]
        m = n[0]
        for i in n[1:]:
            c = max(c+i, i)
            m = max(m, c)
        return m