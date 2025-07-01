class Solution(object):
    def equalPairs(self, grid):
        a = {}
        n = len(grid)
        m= len(grid[0])
        for i in range(m):
            s = ""
            for j in range(n):
                s+=str(grid[j][i]) + ","
            a[s] = a.get(s, 0)+1
        b = 0
        for j in range(n):
            s = ""
            for i in range(m):
                s += str(grid[j][i]) + ","
            if s in a:
                b += a[s]
        return b
        
            
