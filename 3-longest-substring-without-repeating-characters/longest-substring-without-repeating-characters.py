class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = []
        longest = 0
        for c in s:
            if c in ls:
                while c in ls:
                    ls.pop(0)
            
            ls.append(c)
            longest = max(longest, len(ls))
        return longest
