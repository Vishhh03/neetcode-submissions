class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        if len(nums) == 1:      # Edge case
            return nums[0]
        dp[0], dp[1] = nums[0], max(nums[0],nums[1])
        #dp[1] would be the biggest of the first 2 naturally.
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            #two choices, either rob or rob next. no point skipping more than 1 since all number positive
        return dp[-1]