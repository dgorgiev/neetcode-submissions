class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minbuy = prices[0]
        maxp = 0
        for price in prices:
            gain = price - minbuy
            maxp = gain if gain > maxp else maxp
            minbuy = price if price < minbuy else minbuy

        return maxp