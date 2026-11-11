import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def removeSpecialCharacters(text):
            return re.sub(r'[^a-zA-Z0-9\s]', '', text)
        
        res = ""
        rsc_string = removeSpecialCharacters(s)
        string = rsc_string.lower()

        n = len(string)

        for i in range(n-1, -1, -1):
            res += string[i]

        if (res.replace(" ", "") == string.replace(" ", "")):
            return True
        return False        