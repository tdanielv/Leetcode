class Solution:
    def searchRange(self, nums, target):
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if res == False:
            res = [-1, -1]
        res = [res[0], res[-1]]
        return res


print(Solution().searchRange([5,7,7,8,8,10], 8))