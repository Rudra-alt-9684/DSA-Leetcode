class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        if not s:
            return

        for i in range(len(s)):
            if s[i] == '*':
                if not stack:
                    return
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)