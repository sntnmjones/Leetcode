class Solution:
    '''
    neetcode: https://www.youtube.com/watch?v=Vn2v6ajA7U0
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            # Base case
            if i == len(nums):
                res.append(subset.copy())
                return

            # Include subsets with nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Include subsets without nums[i]
            subset.pop()
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res