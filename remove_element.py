def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            print(nums)
        else:
            i += 1

nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)