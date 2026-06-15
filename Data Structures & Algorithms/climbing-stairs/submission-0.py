class Solution:
    def climbStairs(self, n: int) -> int:
        # theres two options each move. climb 1 step or 2 steps.
        dp = [0] * (n+1)
        # dp[0], dp[1] = 1, 1
        # to reach stair i, it will be a sum of possibilites from stair i-1 and stair i-2 because every valid path to 3 will have 2 or 1 before it
        # f(1) = 1, f(0) = 1; WHY? Need base case else i-1 and i-2 goes out of bounds, also easy base case to find out ourselves anyway
        
        #now f(2) = f(1) + f(0) = 1+1 = 2
        def dfs(step):
            if dp[step] != 0:
                return dp[step]
            if step == 0:
                return 1
            if step == 1:
                return 1
            dp[step] = dfs(step-1) + dfs(step-2)
            return dp[step]
        return dfs(n)