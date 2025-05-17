class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        result = 0
        sign = 1
        s = s.lstrip()

        if not s:
            return 0
        
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        for char in s:
            if char.isdigit():
                result = result * 10 + (ord(char) - 48)
            else:
                break

        result *= sign

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result