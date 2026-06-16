class Solution:
    def rob(self, nums: List[int]) -> int:
        # SPACE EFFICIENT METHOD
        
        if len(nums) == 1:      # Edge case
            return nums[0]
        rob1, rob2 = nums[0], max(nums[0],nums[1])
        #dp[1] would be the biggest of the first 2 naturally.
        for i in range(2,len(nums)):
            rob1, rob2 = rob2, max(rob2, rob1+nums[i])
            #two choices, either rob or rob next. no point skipping more than 1 since all number positive
        return rob2