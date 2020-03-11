# 输出版
def findTarget(nums, target):
    l = 0
    h = len(nums)
    while l < h:
        mid = l + (h-l) // 2
        if nums[mid] >= target:
            h = mid
        else:
            l = mid+1
    return l

nums = [5,7,7,8,8,10]
target = 6

first = findTarget(nums, target)
last = findTarget(nums, target+1) -1

if nums[first] != target:
    print([-1,1])
else:
    print([first, max(first,last)])

    # 类版
    #
    # class Solution(object):
    #     def searchRange(self, nums, target):
    #         """
    #         :type nums: List[int]
    #         :type target: int
    #         :rtype: List[int]
    #         """
    #         first = findTarget(nums, target)
    #         last = findTarget(nums, target + 1) - 1
    #
    #         if first == len(nums) or nums[first] != target:
    #             return [-1, -1]
    #         else:
    #             return [first, max(first, last)]
    #
    #
    # def findTarget(nums, target):
    #     l = 0
    #     h = len(nums)
    #     while l < h:
    #         mid = l + (h - l) // 2
    #         if nums[mid] >= target:
    #             h = mid
    #         else:
    #             l = mid + 1
    #     return l