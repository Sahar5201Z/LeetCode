class Solution:
    """def maxProfit(self, prices: List[int]) -> int:
        maximum_profit_loc=[0,0]
        maximum_profit=0
        for i in range (len(prices)-1):
            for j in range(i+1,len(prices)):
                if(prices[j]-prices[i]>maximum_profit):
                   maximum_profit= prices[j]-prices[i]
                   maximum_profit_loc=[i,j]
                
        return maximum_profit"""
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        max_sum = 0
        while j < len(prices):
            if prices[i] >= prices[j] :
                i = j
                                
            else:
                val = prices[j] - prices[i]
                max_sum = max(max_sum,val)
            j += 1
        return max_sum