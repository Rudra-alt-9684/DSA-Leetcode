class Solution:
    def largestPerimeter(self, n: list[int]) -> int:
        n = sorted(n, reverse=True)

        for i in range(len(n) - 2):
            a = n[i]
            b = n[i + 1]
            c = n[i + 2]

            if b + c > a:
                return a + b + c

        return 0