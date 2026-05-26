class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {")": "(", "}": "{", "]": "["}
        c = []
        
        for i in s: 
            print(i)
            if i in d:
                if (len(c) == 0) or (d[i] != c.pop()):
                    return False
            else:
                c.append(i)
        return (len(c)==0)