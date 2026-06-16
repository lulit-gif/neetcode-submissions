class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            signature = ''.join(sorted(word))

            if signature not in group:
                group[signature] = []
                
            group[signature].append(word)
            
        return list(group.values())

        