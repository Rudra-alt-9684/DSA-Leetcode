class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        long_prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(long_prefix):
                long_prefix = long_prefix[:-1]
            if not long_prefix:
                return ""
        return long_prefix


        