def knapsack(items,capacity):
 dp=[0]*(capacity+1)
 for weight,value in items:
  for limit in range(capacity,weight-1,-1):dp[limit]=max(dp[limit],dp[limit-weight]+value)
 return dp[capacity]
if __name__=='__main__':print(knapsack([(2,6),(3,10),(4,12)],5))