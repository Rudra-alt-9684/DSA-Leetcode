class Solution:
    def maxProduct(self, n: list[int]) -> int:
        mx = mn = ans = n[0]

        for i in range(1, len(n)):
            x = n[i]

            if x < 0:
                mx, mn = mn, mx

            mx = max(x, mx * x)
            mn = min(x, mn * x)

            ans = max(ans, mx)

        return ans