class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {")": "(", "}": "{", "]": "["}
        c = []

        for i in s: 
            if i in d: 
                c.pop()
            else:
                c.append(i)
        return (len(c)==0)