class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if (a-c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1

# Code 2
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins == None or len(coins) == 0:
            return 0
        
        dp = [[None for i in range(amount+1)] for j in range(len(coins) + 1)]
        dp[0][0] = 0
        
        for i in range(1,amount+1):
            dp[0][i] = amount + 1
            
        for i in range(1,len(coins) + 1):
            for j in range(0,amount+1):
                if j< coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j],(dp[i][j-coins[i-1]] + 1))
        
        return -1 if dp[len(coins)][amount] == amount + 1 else dp[len(coins)][amount]
