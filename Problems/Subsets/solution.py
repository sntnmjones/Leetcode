'''
Neetcode
https://www.youtube.com/watch?v=REOH22Xwdkk
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def getSubset(i):
            if not i < len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            getSubset(i + 1)

            # Backtrack
            subset.pop()
            getSubset(i + 1)

        getSubset(0)
        return result

'''
Average solution
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(index, path):
            # append current subset
            res.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        
        backtracking(0, path)
        return res
    
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(2^n)
