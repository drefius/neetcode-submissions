class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for idx in range(97,123) :
            character = chr(idx)
            if s.count(chr(idx)) != t.count(chr(idx)):
                return False
        return True
