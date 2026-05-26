class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else: 
                chars[s[i]] = 1

        for j in range(0, len(t)):
            if t[j] in chars and chars[t[j]] > 0:
                chars[t[j]] -= 1
            else:
                return False
        return True