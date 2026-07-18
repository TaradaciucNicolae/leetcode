class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #every_price = ep
        #biggest_price_after_every_price = biggest_price

        min_price = prices[0]
        max_profit = 0

        for every_price in prices:

            if min_price > every_price:
                min_price = every_price


            max_profit=max(max_profit, every_price - min_price)
            
        return max_profit
