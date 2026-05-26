class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {")": "(", "}": "{", "]": "["}
        c = []

        for i in s: 
            c.append(i)

        for j in range(int(len(c)/2)):
            if not c[j] == d[c[-(j+1)]]:
                return False
        return True
