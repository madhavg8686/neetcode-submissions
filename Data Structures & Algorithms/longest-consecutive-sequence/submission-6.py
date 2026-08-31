class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        count=1
        maxcount=1
        if len(nums)==0:
            return 0
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                count=1
            maxcount=max(maxcount,count)
        return maxcount
        