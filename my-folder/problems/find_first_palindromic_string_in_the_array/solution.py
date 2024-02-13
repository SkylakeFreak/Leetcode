class Solution(object):
    def firstPalindrome(self, words):
        Flag=True
        for i in words:
            if i==i[::-1]:
                return i
            else:
                Flag=False 
        if Flag==False:
            return ""                  