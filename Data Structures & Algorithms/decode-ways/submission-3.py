class Solution:
    def numDecodings(self, s: str) -> int:
        #Choices each time -> either take i if above 0 or include i+1 if < 26, if i=0 we have to include i-1 into 0 
        #starting from the last for 1012
        # 2 or 12 -> 1 or 01 OR 0 or 10 => number cannot start with 0 hence we take 1 or 10-> 0 or 10 OR END => we take 10 then END
        memo = {}
        
        def dfs(i):
            if i in memo:           #memoization
                return memo[i]
            
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0
            ways = dfs(i+1)
            if i+1 < len(s) and '10' <= s[i:i+2] <= '26':       #It is i+1 not i, cuz we are checking for two digits so it will prematurely fail otherwise
                ways += dfs(i+2)
            memo[i] = ways      # memoing here before the return
            return ways
        return dfs(0)