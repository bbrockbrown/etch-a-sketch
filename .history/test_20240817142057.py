def findMin(nums) -> int:
    n = len(nums)
    l = 0
    r = n - 1

    if n == 1:
        return nums[0]

    while l <= r:
        mid = (l + r) // 2

        if (nums[mid - 1] > nums[mid]) and (nums[mid] < nums[mid + 1]):
            return nums[mid]
        # case where minimum element is at end of arr
        elif (nums[mid - 1] > nums[mid]) and (nums[mid] < nums[0]) and (mid == (n-1)):
            return nums[mid]
        elif (nums[mid - 1] < nums[mid]) and (nums[mid] < nums[mid + 1]) and (nums[mid] > nums[-1]):
            l = mid + 1
        else:
            r = mid - 1