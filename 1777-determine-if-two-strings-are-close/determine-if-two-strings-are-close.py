class Solution(object):
    def closeStrings(self, word1, word2):
        c = len(word1)
        d = len(word2)
        if c != d:
            return False
        a = {}
        b = {}
        for i in range(len(word1)):
            if word1[i] in a:
                a[word1[i]] += 1
            else:
                a[word1[i]] = 1
        for j in range(len(word2)):
            if word2[j] in b:
                b[word2[j]] += 1
            else:
                b[word2[j]] = 1
        g = sorted(a.values())
        h = sorted(b.values())
        if g != h:
            return False
        e = set(a.keys())
        f = set(b.keys())
        if e != f:
            return False
        return True