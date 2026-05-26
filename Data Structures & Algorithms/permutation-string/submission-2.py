class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        orig = {}
        new = {}
        l = 0

        for j in s1: 
            if j in orig:
                orig[j] += 1
            else: 
                orig[j] = 1
        
        for r in range(len(s2)):

            if s2[r] in new:
                new[s2[r]] += 1
            else: 
                new[s2[r]] = 1
            
            while (sum(new.values()) > len(s1)):
                print(sum(new.values()))
                new[s2[l]] -= 1
                l += 1

            filtered_new = {k: v for k, v in new.items() if v > 0}
                        
            if filtered_new == orig:
                return True

        return False



