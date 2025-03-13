class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenght_s = len(s)
        substrings = []
        for i in range(lenght_s):
            for j in range(lenght_s, i, -1):
                if s[i:j] == s[i:j][::-1] and (j - i > 1):
                    substrings.append(s[i:j])

        if substrings:
            return max(substrings, key=len)
        return s[0]