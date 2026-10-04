class Solution:
    def maxArea(self, h: list[int]) -> int:
        l = 0
        r = len(h) - 1
        c = m = 0
        while l < r:
            ht = min(h[l], h[r])
            w = r - l
            c = ht*w
            m = max(m, c)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return m