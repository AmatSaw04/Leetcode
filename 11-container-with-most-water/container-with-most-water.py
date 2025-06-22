class Solution(object):
    def maxArea(self, height):
        max_water = 0
        i = 0
        j = len(height) - 1
        while i < j:
            a = height[i]
            b = height[j]
            if a<=b:
                area = (j-i)*a
                i+=1
            else:
                area = (j-i)*b
                j-=1
            if area > max_water:
                max_water = area
        return max_water