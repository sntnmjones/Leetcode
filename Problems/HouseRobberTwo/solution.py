class Solution:
    """
    Implement House Robber One twice, skipping the first and last house.
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        cache = {}
        homes = []

        def robbin(i):
            if i < 0:
                return 0
            
            if i in cache:
                return cache[i]

            curHome = homes[i] + robbin(i - 2)
            prevHome = robbin(i - 1)
            cache[i] = max(curHome, prevHome)
            return cache[i]

        # Skip the first house
        homes = nums[1:]
        cache = {0:homes[0]}
        skipFirst = robbin(len(homes) - 1)

        # Skip the last house
        homes = nums[:-1]
        cache = {0:homes[0]}
        skipLast = robbin(len(homes) - 1)

        return max(skipFirst, skipLast)

    """
    House Robber One
        # Top down
        def robbin(i):
            if i < 0:
                return 0

            if i in cache:
                return cache[i]
            
            curHouse = nums[i] + robbin(i - 2)
            prevHouse = robbin(i - 1)
            robbedHouse = max(curHouse, prevHouse)
            cache[i] = robbedHouse
            return robbedHouse
        
        n = len(nums)
        cache = {0:nums[0]}
        return robbin(n - 1)

        # Bottom up
        n = len(nums)
        cache = [0 for _ in nums]
        cache[0] = nums[0]

        for i in range(1, n):
            if i == 1:
                curHouse = nums[i]
            else:    
                curHouse = nums[i] + cache[i - 2]

            prevHouse = cache[i - 1]
            maxHouse = max(curHouse, prevHouse)
            cache[i] = maxHouse

        return cache[n - 1]
    """