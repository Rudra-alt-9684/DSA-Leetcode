
class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        rev = []

        for i in range(len(str_x) - 1, -1, -1):
            if str_x[i].isalnum():
                rev.append(str_x[i])

        res = int(''.join(rev))

        if x < 0:
            res = -res

        if res < -(2**31) or res > 2**31 - 1:
            return 0

        return res
