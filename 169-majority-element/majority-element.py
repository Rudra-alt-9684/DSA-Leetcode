class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m = nums[0]
        c = 1

        for i in range(1, len(nums)):
            if nums[i] == m:
                c += 1
            else:
                c -= 1

            if c == 0:
                m = nums[i]
                c = 1

        return m