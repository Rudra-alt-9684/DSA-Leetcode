
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        res = []
        nums = '0123456789'
        sign = 1
        j = 0

        if s[j] == '-':
            sign = -1
            j += 1
        elif s[j] == '+':
            j += 1

        for i in range(j, len(s)):
            if s[i] in nums:
                res.append(s[i])
            else:
                break

        if not res:
            return 0

        num = 0
        for digit in res:
            num = num * 10 + nums.index(digit)

        num *= sign

        return max(-2**31, min(num, 2**31 - 1))
