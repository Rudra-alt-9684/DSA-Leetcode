class Solution:
    def heightChecker(self, h: list[int]) -> int:
        e = sorted(h)
        c = 0

        for i in range(len(h)):
            if e[i] != h[i]:
                c += 1

        return c 

        