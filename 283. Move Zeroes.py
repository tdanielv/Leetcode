class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = nums.count(0)
        for i in range(k):
            nums.remove(0)
        for i in range(k):
            nums.append(0)
        return nums