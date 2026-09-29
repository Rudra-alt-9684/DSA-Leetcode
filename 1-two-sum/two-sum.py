class Solution:
    def twoSum(self, n: list[int], t: int) -> list[int]:
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i] + n[j] == t:
                    return [i,j]
        