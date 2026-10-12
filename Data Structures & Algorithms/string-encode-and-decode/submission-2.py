class Solution:

    def strEncode(self, st):
        final = ""
        for s in st:
            final += str(ord(s))
            final += ","
        return final[:-1] 

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NIL"
        finalFinal = ""
        for st in strs:
            finalFinal += self.strEncode(st)
            finalFinal += ":"
        return finalFinal[:-1]

    def strDecode(self, st):
        final = ""
        stList = st.split(",")
        for st in stList:
            if len(st) > 0:
                final += chr(int(st))
        return final

    def decode(self, s: str) -> List[str]:
        if s == "NIL":
            return []
        return [self.strDecode(st) for st in s.split(":")]
         