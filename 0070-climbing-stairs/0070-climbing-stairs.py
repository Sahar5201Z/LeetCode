class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        ways = [0] * n
        ways[0] = 1  # There is only 1 way to reach the first step
        ways[1] = 2  # There are 2 ways to reach the second step

        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[-1] 

        