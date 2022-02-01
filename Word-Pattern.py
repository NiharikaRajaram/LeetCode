class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d2 = {}
        
        words = s.split()
        if len(pattern) != len(words):
            return False
        i = 0
        
        while i < len(words):
            if words[i] not in d and pattern[i] not in d2:
                d[words[i]] = pattern[i]
                d2[pattern[i]] = True
            elif d.get(words[i]) != pattern[i]:
                return False
            i += 1
        
        return True
