class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m: return False

        d1 = dict()
        d2 = dict()
        for i in range(n):
            c1 = s[i]
            c2 = t[i]
            d1[c1] = d1.get(c1, 1) + 1
            d2[c2] = d2.get(c2, 1) + 1
        return d1 == d2
        