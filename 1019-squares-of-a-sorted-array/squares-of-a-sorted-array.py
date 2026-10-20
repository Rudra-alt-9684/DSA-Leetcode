class Solution:
    def sortedSquares(self, n: list[int]) -> list[int]:
        l = 0
        r = len(n) - 1
        res = []

        while l <= r:
            ls = n[l] * n[l]
            rs = n[r] * n[r]

            if ls > rs:
                res.append(ls)
                l += 1
            else:
                res.append(rs)
                r -= 1

        return res[::-1]