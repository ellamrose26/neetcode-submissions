class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums=sorted(nums)
        for i in range(length):
            if i + 1 < length:
                if nums[i+1] - nums[i] != 1:
                    return nums[i] + 1
            else:
                if nums[0] != 0:
                    return 0
                else:
                    return length