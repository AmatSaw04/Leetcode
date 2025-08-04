class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.strip().split(" ")
        return len(a[-1])
        