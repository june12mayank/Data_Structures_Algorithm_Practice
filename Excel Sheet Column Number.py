# Given a string columnTitle that represents the column title as appear in an Excel sheet,
#  return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r=0
        d={}
        for i in range(1,27):
            d[chr(ord('A')+i-1)]=i
        for c in columnTitle:
            r=r*26+d[c]
        return r