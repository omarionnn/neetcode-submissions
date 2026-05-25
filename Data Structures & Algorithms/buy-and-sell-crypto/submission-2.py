class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return 0

        left = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                curr_profit = prices[right] - prices[left]
                profit = max(profit, curr_profit)

        return profit 

        