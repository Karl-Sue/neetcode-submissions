class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(0,len(strs)):
            encoded = encoded + str(len(strs[i])) + "#" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        str1 = s.strip()
        result = []
        while i<len(str1):
            start = str1.index("#",i)
            sLen = int(str1[i:start])
            result.append(str1[start+1:start+sLen+1])
            i = start + sLen+1
        return result