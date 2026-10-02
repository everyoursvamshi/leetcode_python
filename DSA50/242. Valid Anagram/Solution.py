class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        #as it contains only lower alphabets
        alphabet_counts=[0]*26
        for alpha in s:
            alphabet_counts[ord(alpha)-ord('a')]+=1
        for alpha in t:
            alphabet_counts[ord(alpha)-ord('a')]-=1
        for counts in alphabet_counts:
            if counts!=0:
                return False
        return True
