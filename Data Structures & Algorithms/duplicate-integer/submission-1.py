class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doubles = []
        for num in nums:
            if num not in doubles:
                doubles.append(num)
        print(nums)
        print(doubles)
        if len(doubles)<len(nums):
            return True
        else:
            return False
      