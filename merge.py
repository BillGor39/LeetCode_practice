
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[m:] = nums2[0:n]
    nums1.sort()
