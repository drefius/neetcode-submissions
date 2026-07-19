class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letter = [0]*26
        for s_ in s:
            letter[ord(s_) - ord('a')] += 1
        
        for t_ in t:
            letter[ord(t_) - ord('a')] -= 1
        
        for le_ in letter:
            if le_ != 0: return False
        return True