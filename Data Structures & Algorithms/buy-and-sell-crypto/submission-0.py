class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #possible profits = local max - local min, where local_max_j > local_min_i
        #max profit = max of all possible profits

        local_max = 0
        local_min = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            price = prices[i]
            if(price < local_min):
                #no local max, so set current to local_max
                local_min = price
                local_max = price
            else:
                local_max = max(local_max, price)
            max_profit = max(max_profit, local_max - local_min)
        return max_profit




        