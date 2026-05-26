class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxx = 0

        for i in range(len(s)):
            inst = []
            lm = 0
            while (i+lm < len(s)) and (s[i+lm] not in inst):
                inst.append(s[i+lm])
                lm += 1
            maxx = max(maxx, lm)
        return maxx
