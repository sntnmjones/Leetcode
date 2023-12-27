class Solution:
    '''
    https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(perm, visited):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for i in range(len(nums)):
                if not nums[i] in perm:
                    perm.append(nums[i])
                    # visited.add(nums[i])
                    helper(perm, visited)
                    perm.pop()
                    # visited.remove(nums[i])

        helper([], set())
        return result