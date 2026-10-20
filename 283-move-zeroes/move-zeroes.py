class Solution:
    def moveZeroes(self, n: list[int]) -> None:
        l = 0
        for r in range(len(n)):
            if n[r] != 0:
                n[l], n[r] = n[r], n[l]
                l = l+1
            
        