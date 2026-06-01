class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = ""
        right = ""
        word = s.replace(" ", "").lower()
        word2 = re.sub(r'[^a-zA-Z0-9]', '', word)
        
        l = len(word2)//2
        l2 = len(word2)
        for i in range(l):
            left = left + word2[i]
            right = right + word2[l2-1-i]
        print(left, right)
        return left == right