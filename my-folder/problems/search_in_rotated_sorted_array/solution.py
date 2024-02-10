class Solution(object):
    def search(self, nums, target):
        try:
            temp=nums.index(target)
        except:
            return -1    
        return temp
        