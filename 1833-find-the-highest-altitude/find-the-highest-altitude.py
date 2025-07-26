class Solution(object):
    def largestAltitude(self, gain):
        i = 0
        a = 0
        for j in gain:
            i += j
            if i > a:
                a = i
        return a
        

        