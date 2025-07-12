class Solution(object):
    def predictPartyVictory(self, senate):
        a  = []
        b = []
        e = len(senate)
        for i, s in enumerate(senate):
            if s == "R":
                a.append(i)
            else:
                b.append(i)
        while a and b:
            c = a.pop(0)
            d = b.pop(0)
            if c < d:
                a.append(c+e)
            else:
                b.append(d+e)
        return "Radiant" if a else "Dire"




        
        