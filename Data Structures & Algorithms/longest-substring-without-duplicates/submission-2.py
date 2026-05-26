class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cset = set()
        maxx = 0
        l = 0

        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            maxx = max(maxx, len(cset))

        return maxx