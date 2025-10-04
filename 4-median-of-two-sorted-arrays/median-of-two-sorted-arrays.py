class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=sorted(nums1+nums2)
        n=len(nums)
        if n%2!=0:
            mid=n//2
            return float(nums[mid])
        else:
            mid1=n//2-1
            mid2=n//2
            res=(nums[mid1]+nums[mid2])/2.0
            return res
        