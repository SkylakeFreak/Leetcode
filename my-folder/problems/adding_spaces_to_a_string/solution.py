from array import array
class Solution(object):
    def addSpaces(self, s, spaces):
        chararray=array('u',s)
        count=0
        for pos in spaces:
            chararray.insert(pos+count,' ')
            count+=1
        res=chararray.tounicode()        
        return res    
        