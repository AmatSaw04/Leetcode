class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a = ""
        c = {}
        for i in s:
            if i in a:
                c[len(a)] = a
                j = a.find(i)
                a = a[j+1:]
            a += i
        if a:
            c[len(a)] = a
        if not a:
            return 0
        return max(c.keys())
        
