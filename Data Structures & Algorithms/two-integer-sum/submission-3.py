class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} 
        for i, num in enumerate(nums):
            print (num,i)
            required = target - num
            if required in map:
                return [map[required], i]
            map[num] = i
        return []