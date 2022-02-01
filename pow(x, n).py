class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1
        result = self.myPow(x, int(n/2))
        # print(type(result))
        # (+ve, -ve) even
        if n%2 == 0:
            return result * result
        # (+ve) odd
        elif n > 0: 
            return result * result * x
        # (-ve) odd
        else: 
            return result * result * (1/x)
