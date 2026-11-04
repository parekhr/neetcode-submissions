class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        highest_profit = 0
        lowest_price_seen = prices[0]

        for i in range(len(prices)):
            if prices[i] < lowest_price_seen:
                lowest_price_seen = prices[i]
            temp = prices[i] - lowest_price_seen
            if temp > highest_profit:
                highest_profit = temp
        return highest_profit