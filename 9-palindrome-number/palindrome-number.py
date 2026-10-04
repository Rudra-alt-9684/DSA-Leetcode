class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        sx = list(str(x))
        rx = sx[::-1]
        return rx == sx