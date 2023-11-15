class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        recent_highest_k = 0
        while l <= r:
            k = (l + r) // 2

            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile / k)

            if total_hours > h:
                l = k + 1
            else:
                # Track the largest k value, while trying to get lower
                recent_highest_k = k
                r = k - 1

        return recent_highest_k