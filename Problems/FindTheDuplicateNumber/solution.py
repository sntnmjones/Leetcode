class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-duplicate-number/solutions/3236488/287-solution-with-step-by-step-explanation/
        # Using Floyd's Tortoise and Hare algorithm
        # to detect the cycle in the linked list
        slow = nums[0]
        fast = nums[0]
        
        # Move tortoise and hare until they meet
        # (Detect the cycle using Floyd's cycle detection)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Reset tortoise to the start of the list
        slow = nums[0]
        
        # Move tortoise and hare at the same speed until they meet again
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # Return the duplicate number
        return slow