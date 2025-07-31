class Solution(object):
    def longestCommonPrefix(self, strs):
        a = strs[0]
        res = ""
        for i, char in enumerate(a):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return a[:i]

        return strs[0]
