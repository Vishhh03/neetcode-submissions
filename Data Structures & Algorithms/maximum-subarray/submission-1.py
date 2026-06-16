class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Cleaner Solution, since two pointer not needed

        result = nums[0]
        curr = nums[0]
        if len(nums)>1:
            for i in range(1,len(nums)):
                num = nums[i]
                curr = max(num, num+curr)
                result = max(curr, result)
        return result