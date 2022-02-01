class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == None or t == None or len(s) == 0 or len(t) == 0 or len(s)!=len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for i in range(0,len(s)):
            s_c = s[i]
            t_c = t[i]
            
            if s_c not in s_to_t:
                s_to_t[s_c] = t_c
            if t_c not in t_to_s:
                t_to_s[t_c] = s_c
            if s_to_t[s_c] != t_c or t_to_s[t_c] != s_c:
                return False
            # print("s_to_t ", s_to_t)
            # print("t_to_s ", t_to_s)
        return True
