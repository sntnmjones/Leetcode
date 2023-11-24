class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestSub = 0
        l_p = 0
        letterCount = {}

        for r_p in range(len(s)):
            # Add current letter to count
            letterCount[s[r_p]] = letterCount.get(s[r_p], 0) + 1
            
            # Calculate the number of letters that need replaced
            numToReplace = ((r_p - l_p) + 1) - max(letterCount.values())

            if (numToReplace > k):
                letterCount[s[l_p]] -= 1
                l_p += 1

            longestSub = max(longestSub, (r_p - l_p) + 1)
        
        return longestSub