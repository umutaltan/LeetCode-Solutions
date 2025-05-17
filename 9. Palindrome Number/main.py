class Solution:
    def isPalindrome(self, x: int) -> bool:
        ispalind = 0
        if x<0:
            return False
        y = str(x)
        for i in range(len(y)):
            if y[i] == y[len(y)-i-1]:
                ispalind = 1 
            else:
                ispalind = 0
                return False
        return True