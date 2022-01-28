class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 0, num//2
        
        while left <= right:
            pivot = left + (right - left) // 2
            n = pivot * pivot
            
            if n > num:
                right = pivot - 1
            elif n < num:
                left = pivot + 1
            else:
                return True
        return False
