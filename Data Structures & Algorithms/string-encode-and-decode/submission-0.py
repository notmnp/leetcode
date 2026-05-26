class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""
        for i in strs:
            string += i + " "
        return string

    def decode(self, s: str) -> List[str]:

        checkpoint = 0
        l = []
        for i in str[0]:
            if i == " ":
                list.append(str[checkpoint:i])