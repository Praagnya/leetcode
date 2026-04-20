class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         HashMap = {}
         start = 0 
         best = 0
         for i, ch in enumerate(s): 
            if ch in HashMap: 
                start = max(start, HashMap.get(ch))
            best = max(best, (i - start +1 ))
            HashMap[ch] = i + 1
         return best 