class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs: 
            # sort each word and use it as a key 
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        # return all grouped anagrams 
        return list(anagrams.values())



          