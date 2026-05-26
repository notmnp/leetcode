class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # 26 possible letters, so iterating is O(26)
        maxx = 0
        l = 0
        lcount = {}

        for r in range(len(s)):

            if s[r] in lcount:
                    lcount[s[r]] += 1
            else:
                lcount[s[r]] = 1
            
            while (r < len(s)) and (((r-l) + 1) - max(lcount.values(), default=0) > k):
                lcount[s[l]] -= 1
                l += 1
                    
            maxx = max(maxx, (r - l + 1))

        return maxx
            