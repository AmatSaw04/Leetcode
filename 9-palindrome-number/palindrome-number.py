class Solution(object):
    def isPalindrome(self, x):
        
        a = False

        if str(x) ==str(x)[::-1]:
            a = True
        return a
