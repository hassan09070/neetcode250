class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            # grow outward while it's still a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # loop stopped one step too far, so step back in
            return s[l + 1:r]

        for i in range(len(s)):
            odd = expand(i, i)        # center is one char:  "aba"
            even = expand(i, i + 1)   # center is two chars: "abba"

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even

        return res