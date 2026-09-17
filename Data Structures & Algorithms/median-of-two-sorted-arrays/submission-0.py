class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1=sorted(nums1)
        if len(nums1)%2==0:
            mid=(len(nums1)//2)-1
            median=(nums1[mid]+nums1[mid+1])/2
        if len(nums1)%2==1:
            mid=len(nums1)//2
            median=nums1[mid]
        return median

        