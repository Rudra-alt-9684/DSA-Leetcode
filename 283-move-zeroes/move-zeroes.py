class Solution:
    def moveZeroes(self, a: list[int]) -> None:
        p = 0
        for i in range(len(a)):
            if a[i] != 0:
                a[i], a[p] = a[p], a[i]
                p += 1
        return a
        
        