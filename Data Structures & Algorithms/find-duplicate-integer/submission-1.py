class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        HashMap={}
        for i in nums:
            if i in HashMap:
                return i
            else:
                HashMap[i]=1
                


        