class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        flag = True
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return flag
        flag = False
        return flag

        