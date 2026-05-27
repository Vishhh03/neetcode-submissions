class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        right = n-1
        left = 0
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum > target:
                right -=1
            else:
                left += 1
        return

#  1 2 4 5 8
# TARGET = 7
#