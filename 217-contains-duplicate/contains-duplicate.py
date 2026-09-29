class Solution:
    def containsDuplicate(self, n: list[int]) -> bool:
        len_n = len(n)
        len_setn = len(set(n))
        return len_n != len_setn
        