class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            #print(nums.count(i))
            if nums.count(i)>1:
                return True
        else:
            return False
            