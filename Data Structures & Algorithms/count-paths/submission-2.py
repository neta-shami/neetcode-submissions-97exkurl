class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [1] * n
        for _ in range(1 , m):
            for j in range(n-1):
                dp[j + 1] += dp[j]

        return dp[n-1]

            

        