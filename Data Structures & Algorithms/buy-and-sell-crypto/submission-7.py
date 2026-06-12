class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        map  = {}
        l = 0
        profit = 0
        for r in range(1,len(prices)):
            if prices[r]> prices[l]:
                profit = max(profit, prices[r] - prices[l])
                
            else:
                l = r       # Not l += 1, but l=r since else happens only when a 
                            # lesser price has been identified by right pointer

        return profit