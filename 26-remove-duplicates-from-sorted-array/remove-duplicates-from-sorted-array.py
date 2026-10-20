class Solution:
    def removeDuplicates(self, n: list[int]) -> int:
        if not n:
            return 0

        l = 0

        for r in range(1, len(n)):
            if n[l] != n[r]:
                l += 1
                n[l] = n[r]

        return l + 1