class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = {}
        result = []
        for word in strs:
            key = "".join(sorted(word))
            strdict[key] = strdict.get(key,[]) + [word]
        for pair in strdict.values():
            result.append(pair)
        return result