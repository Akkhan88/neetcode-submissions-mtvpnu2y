class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        for c in s:
            if c in count1: 
                count1[c] = count1[c] + 1 
            else: 
                count1[c] = 1 
        count2 = {}
        for c in t:
            if c in count2: 
                count2[c] = count2[c] + 1 
            else: 
                count2[c] = 1 
        return count1 == count2