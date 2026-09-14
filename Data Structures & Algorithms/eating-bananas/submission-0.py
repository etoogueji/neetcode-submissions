import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            
            # Compute total hours needed at speed k
            total_hours = sum(math.ceil(p / k) for p in piles)

            if total_hours <= h:
                res = k  # Valid speed found, save it
                right = k - 1  # Try searching for a smaller speed
            else:
                left = k + 1  # Speed is too slow, increase speed

        return res