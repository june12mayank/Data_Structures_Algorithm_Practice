# Find the maximum profit you can achieve. You may complete as many transactions as you like
# We find lowest dip by continous decreasing end and peak by continous increasing series.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        N=len(prices)
        buy=prices[0]
        sell=prices[0]
        profit=0
        while(i<N-1):
            while((i<N-1) and (prices[i]>=prices[i+1])):
                i+=1
            buy =prices[i]
            while(i<N-1 and prices[i]<=prices[i+1]):
                i+=1
            sell=prices[i]
            profit+=sell-buy
        return profit
                