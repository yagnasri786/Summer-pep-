class Solution:
    def maxProfit(self, prices):
        buy = -prices[0]
        sell = 0
        cooldown = 0

        for i in range(1, len(prices)):
            prev_buy = buy
            prev_sell = sell
            prev_cooldown = cooldown

            buy = max(prev_buy, prev_cooldown - prices[i])
            sell = prev_buy + prices[i]
            cooldown = max(prev_cooldown, prev_sell)

        return max(sell, cooldown)