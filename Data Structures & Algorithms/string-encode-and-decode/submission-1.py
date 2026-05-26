class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""
        for i in strs:
            string += i + " "
        return string

    def decode(self, s: str) -> List[str]:

        checkpoint = 0
        l = []
        for i in range(len(s)):
            if s[i] == " ":
                l.append(s[checkpoint:i])
                checkpoint = i + 1
        return l
