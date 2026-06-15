class Solution:
    def climbStairs(self, n: int) -> int:
            #BOTTOMS UP APPROACH
            # Solution 2 uses O(n) space, this uses O(1) or rather O(2)
        # dp = [0,0]
        # dp[0], dp[1] = 1,1
        # for step in range(2,n+1):
        #     dp[step%2] = dp[0]+dp[1]
        #     result = dp[step%2]
        # return dp[n] if n <2 else result

        if n < 2:
            return 1
        prev1 = 1
        prev2 = 1
        for step in range(2,n+1):
            prev1, prev2 = prev1+prev2, prev1
        return prev1    
        