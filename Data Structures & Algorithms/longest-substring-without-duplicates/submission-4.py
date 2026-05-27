class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        freq = {}
        l, r = 0, 0

        while r <= len(s)-1 : 
            
            freq[s[r]] = freq.get(s[r], 0) + 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
        
            r += 1
            
            longest = max(longest, r-l)

        return longest