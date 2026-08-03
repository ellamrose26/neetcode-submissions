class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target in nums:
            for i in range(length):
                if nums[i] == target:
                    return i
        else:
            return -1