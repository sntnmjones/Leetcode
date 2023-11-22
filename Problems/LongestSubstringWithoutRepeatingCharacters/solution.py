class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)        
        longestSubstr = 0
        subStr = set()
        l_p = 0

        for r_p in range(n):
            # Move left pointer
            while s[r_p] in subStr:
                subStr.remove(s[l_p])
                l_p += 1

            subStr.add(s[r_p])

            # Add one to difference because 0 indexed
            longestSubstr = max(longestSubstr, (r_p - l_p) + 1)

        return longestSubstr