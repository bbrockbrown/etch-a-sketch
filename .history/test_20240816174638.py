def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # element in nums where elements on either side of desired are greater 
    mini = -5000
    n = len(nums)
    l = 0
    r = n - 1

    if n == 1:
        return nums[0]

    while l <= r:
        mid = (l + r) // 2

        if mid == n - 1:
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[0]:
                return nums[mid]
            else:
                r = mid - 1

        # elements on either side are greater --> minimum number
        if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif nums[mid - 1] < nums[mid] and not (nums[mid] < nums[mid + 1]):
            l = mid + 1
        elif nums[mid] < nums[mid + 1]:
            r = mid - 1
            
            
print(findMin([2,3,4,5,1]))