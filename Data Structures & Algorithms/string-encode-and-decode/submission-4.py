class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""
        for i in strs:
            string += i + "/~"
        return string

    def decode(self, s: str) -> List[str]:

        checkpoint = 0
        l = []
        for i in range(len(s)):
            if s[i] == "/" and s[i+1] == "~":
                l.append(s[checkpoint:i])
                checkpoint = i + 2
        return l


