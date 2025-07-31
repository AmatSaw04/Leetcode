class Solution(object):
    def longestCommonPrefix(self, strs):
        a = strs[0]
        for s in strs[1:]:
            while s.find(a) != 0 :
                a = a[:-1]
                if not a:
                    return ""
        return a