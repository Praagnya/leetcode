class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return false
        mapping_s = {}
        mapping_t = {}

        # Case 1: No mapping exists in either of the dictionaries
        for c1, c2 in zip(s, t):
            if (c1 not in mapping_s) and (c2 not in mapping_t):
                mapping_s[c1] = c2
                mapping_t[c2] = c1

        # Case 2: Either mapping doesn't exist in one of the dictionaries or Mapping exists and it doesn't match in either of the dictionaries or both 
            elif mapping_s.get(c1) != c2 or mapping_t.get(c2) != c1:
                return False 
        
        return True 
        