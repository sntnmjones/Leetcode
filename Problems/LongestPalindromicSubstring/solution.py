class Solution:
    '''
    https://www.youtube.com/watch?v=XYQecbcd6_c
    This is considered dynamic programming because the result 
    is stored in variables outside the loop.
    '''
    def longestPalindrome(self, s: str) -> str:
        self.resLen = 0
        # self.res = ""

        # def findPalindromeA(l, r):
        #     """
        #     n cubed due to slice copies list
        #     """
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > self.resLen:
        #             self.res = s[l : r + 1]
        #             self.resLen = r - l + 1
        #         l -= 1
        #         r += 1

        # for i in range(len(s)):
        #     # odd length
        #     l, r = i, i
        #     findPalindromeA(l, r)

        #     # even length
        #     l, r = i, i + 1
        #     findPalindromeA(l, r)

        # return self.res

        self.resL, self.resR = 0, 0
        def findPalindromeB(l, r):
            """
            n squared solution copies list outside of loop
            """
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = (r - l) + 1
                if curLen > self.resLen:
                    self.resL, self.resR = l, r
                    self.resLen = curLen
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length
            l, r = i, i
            findPalindromeB(l, r)

            # even length
            l, r = i, i + 1
            findPalindromeB(l, r)

        # resR + 1 because slices range is n - 1
        return s[self.resL : self.resR + 1]