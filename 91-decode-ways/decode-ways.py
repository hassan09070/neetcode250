class Solution:
    def numDecodings(self, s: str) -> int:
        # A memoization dictionary to store results of subproblems
        memo = {}

        def algo(i):
            # If we've reached the end of the string, we found 1 valid decoding way
            if i == len(s):
                return 1
            
            # If the current character is '0', it can't start a valid code
            if s[i] == '0':
                return 0
            
            # If we already calculated the answer for this index, return it
            if i in memo:
                return memo[i]

            # Decision 1: Take the current single digit
            res = algo(i + 1)

            # Decision 2: Take two digits (if within bounds and <= "26")
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                res += algo(i + 2)

            # Save the result in the memo map
            memo[i] = res
            return res

        return algo(0)