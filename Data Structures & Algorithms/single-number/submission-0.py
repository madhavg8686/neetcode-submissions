class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        HashMap={}
        for i in nums:
            if i in HashMap:
                HashMap[i]+=1
            else:
                HashMap[i]=1
        for i in HashMap:
            if HashMap[i]==1:
                return i
        