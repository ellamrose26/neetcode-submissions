class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check=[]
        for num in nums:
            if num in check:
                repeat = num
            else:
                check.append(num)
        return repeat
            