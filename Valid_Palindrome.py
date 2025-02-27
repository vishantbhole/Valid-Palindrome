class Solution(object):
    def isPalindrome(self, s):
     
        string = ""
        for a in s:
            if a.isalnum():
                string += a.lower()
        return string == string[::-1]
