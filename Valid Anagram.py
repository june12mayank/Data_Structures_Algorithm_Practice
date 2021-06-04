#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=len(s)
        t1=len(t)
        if s1!=t1:
            return False
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in t:
            if j in d:
                d[j]-=1
            else:
                return False
        for a in d.values():
            if a!=0:
                return False
        return True
        