class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        result=[]

        for i in range(length):
            for j in range(i+1, length):
                if numbers[i] + numbers[j] ==target:
                    result.append(i+1)
                    result.append(j+1)
        return result
