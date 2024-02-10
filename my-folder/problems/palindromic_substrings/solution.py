class Solution(object):
    def countSubstrings(self, s):
        a=s
        point=1
        array=[]
        for j in range(0,len(a)):
            for i in range(0,len(a)-point+1):
                te=a[i:i+point]
                if te==te[::-1]:
                    array.append(te)
            point+=1
        return len(array)                  
        