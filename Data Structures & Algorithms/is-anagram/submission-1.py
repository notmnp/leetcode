class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        composition1 = {}
        composition2 = {}
    
        for i in range(len(s)):
            if composition1.get(s[i]):
                composition1[s[i]] += 1
            else:
                composition1[s[i]] = 1

        for j in range(len(t)):
            if composition2.get(t[j]):
                composition2[t[j]] += 1
            else:
                composition2[t[j]] = 1

        if composition1 == composition2:
            return True
        else:
            return False
