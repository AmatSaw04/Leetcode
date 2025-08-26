import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        aa = 0
        bb = 0
        for x, y in dimensions:
            a = x ** 2 + y ** 2
            b = x * y
            if a > aa:
                aa = a
                bb = b
            if a == aa:
                bb = max(bb,b)
        return bb
        