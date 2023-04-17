class Solution:
    def searchInsert(self, nums, target) -> int:
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == target:
                return i
            elif nums[i]> target:
                return i
            elif nums[-1] < target:
                return len(nums)
            elif nums[0] > target:
                return 0

print(Solution().searchInsert([1,3,5,6], 5))