class Solution(object):
    def asteroidCollision(self, asteroids):
        a = []
        for i in asteroids:
            while a and a[-1] > 0 and i < 0:
                if a[-1] + i < 0:
                    a.pop()
                elif a[-1] + i > 0:
                    break
                else:
                    a.pop()
                    break
            else:
                a.append(i)
        return a
