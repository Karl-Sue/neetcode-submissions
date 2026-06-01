class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        else:
            lst1 = list(s)
            lst2 = list(t)
            lst1.sort()
            lst2.sort()
            for i in range(0,len(lst1)):
                if lst1[i] == lst2[i]: continue;
                else: return False;
            return True;        