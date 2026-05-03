class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
            
        map = {}  
        for ch in s:
            if ch in map:
                map[ch] += 1 
            else:
                map[ch] = 1
        
        for c in t:
            if c in map:
                map[c] -= 1
            else:
                return False
        
        for val in map:
            if map[val] != 0:
                return False
        return True