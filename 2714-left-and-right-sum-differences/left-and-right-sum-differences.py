class Solution:
    def leftRightDifference(self, n: List[int]) -> List[int]:
        s = 0
        nl = []
        nl.append(0)
        for i in range(len(n)-1):
            s += n[i]
            nl.append(s)
        
        s = sum(n)
        nr = []
        for i in range(len(n)-1):
            s -= n[i]
            nr.append(s)
        nr.append(0)

        r = []
        for i in range(len(n)):
            r.append(abs(nr[i] - nl[i]))

        return r
        