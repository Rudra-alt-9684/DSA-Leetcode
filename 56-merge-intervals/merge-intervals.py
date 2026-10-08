class Solution:
    def merge(self, i: list[list[int]]) -> list[list[int]]:
        i.sort()
        r = []
        for j in i:
            if not r or r[-1][1] < j[0]:
                r.append(j)
            else:
                r[-1][1] = max(r[-1][1], j[1])
        return r
        