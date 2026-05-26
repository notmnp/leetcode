class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {")": "(", "}": "{", "]": "["}
        c = []

        for i in s: 
            print(i)
            if i in d:
                if (d[i] != c.pop()):
                    return False
            else:
                c.append(i)
        return (len(c)==0)