class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in s: 
            if i in s_map:
                s_map[i] += 1
            else: 
                s_map[i] = 1
        
        for j in t: 
            if j in t_map: 
                t_map[j] += 1
            else:
                t_map[j] = 1
        
        return t_map == s_map
        