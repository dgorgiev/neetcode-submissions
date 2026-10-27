class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_max = 0
        for i in range(len(prices)):
            maxp = 0
            pi = prices[i]
            for j in range(i, len(prices)):
                p = prices[j] - pi
                maxp = p if p > maxp else maxp
            tot_max = maxp if maxp > tot_max else tot_max

        return tot_max