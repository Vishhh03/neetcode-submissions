class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        if prices:
            for right in range(1,len(prices)):
                if prices[left] == prices[right]:
                    left = right
                elif prices[left] > prices[right]:
                    while prices[left] > prices[right]:
                        left += 1
                else:
                    profit = prices[right] - prices[left]
                    res = max(profit, res)
        return res

            