class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        max_profit = 0
        for i in range(days):
            for j in range(i+1, days):
                if prices[j] > prices[i]: 
                    print(prices[j])
                    print(prices[i])
                    profit = prices[j] - prices[i]
                    if profit> max_profit:
                        max_profit=profit
                    
                else:
                    profit = 0
        return max_profit