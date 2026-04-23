class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}
        for ch in strs:
            new_val = sorted(ch)
            new = ''.join(new_val)

            if new not in map:
                map[new] = [ch]
            else:
                map[new].append(ch)
        
        val = list(map.values())
        return val