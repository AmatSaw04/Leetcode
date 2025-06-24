class Solution(object):
    def maxVowels(self, s, k):
        vowels = {"a","e","i","o","u"}
        a = 0
        left =0
        for i in range(k):
            if s[i] in vowels:
                a += 1
        b = a
        for i in range(k,len(s)):
            if s[left] in vowels:
                a-=1
            left+=1
            if s[i] in vowels:
                a+=1
            b =max(b,a)
        return b