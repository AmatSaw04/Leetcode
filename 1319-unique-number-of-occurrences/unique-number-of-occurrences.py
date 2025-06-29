class Solution(object):
    def uniqueOccurrences(self, arr):
        a = {}
        for i in arr:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        b = list(a.values())
        c= set(a.values())
        return len(b) == len(c)


        