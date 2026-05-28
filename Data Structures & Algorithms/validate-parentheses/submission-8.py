class Solution:
    def isValid(self, s: str) -> bool:
        
        compliment = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else: 
                if len(stack) == 0 or stack.pop() != compliment[s[i]]:
                    return False
        return len(stack) == 0
