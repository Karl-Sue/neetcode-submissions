class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(0,len(strs)):
            encoded = encoded + str(len(strs[i])) + "#" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i<len(s):
            start = s.index("#",i)
            sLen = int(s[i:start])
            result.append(s[start+1:start+sLen+1])
            i = start + sLen+1
        return result