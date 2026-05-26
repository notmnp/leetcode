class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        cset = set()
        maxx = 0
        l = 0

        for r in range(len(s)):
            switch = 0
            while (r < len(s)) and ((s[r] in cset) or switch < k):
                if (s[r] not in cset) and (len(cset) > 0): 
                    switch += 1
                else:
                    cset.add(s[r])
                print(s[r], cset)
                r += 1
            maxx = max(maxx, r-l)
            cset.remove(s[l])
            l += 1

        return maxx

