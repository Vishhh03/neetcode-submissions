class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        map  = {}
        l = 0
        profit = 0
        for r in range(1,len(prices)):
            if prices[r]> prices[l]:
                profit = max(profit, prices[r] - prices[l])
                
            else:
                l = r

        return profit