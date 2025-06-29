class Solution(object):
    def uniqueOccurrences(self, arr):
        a = {}
        for i in arr:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        b = list(a.values())
        b.sort()
        for k in range(len(b)-1):
            if b[k] == b[k+1]:
                return False
        return True
            

        