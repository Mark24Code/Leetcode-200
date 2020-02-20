# 排序求解（2）
#1/2 输入输出版
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
#
# nums.sort()
# print(nums[len(nums) - k])
# 类版
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         nums.sort()
#         return nums[len(nums) - k]

# 大顶堆求解（2）
# 1/2 输入输出
# import heapq
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
#
# print(heapq.nlargest(k, nums)[k-1])
#
# 2/2 类
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#
#         return heapq.nlargest(k, nums)[k - 1]

# 快排求解（2）
# 1/2 输入输出版
nums = [2,1]
k = 2

def quickSort(left, right):
    key = nums[right]                                           # 本算法中，基准值初始化放在数组尾
    location = left
    for i in range(left, right):
        if nums[i] < key:
            nums[i], nums[location] = nums[location], nums[i]
            location = location + 1                             # location始终指向大和小的分界点
    nums[location], nums[right] = nums[right], nums[location]
    return location                                             # location即为第x个最小元素

def findResult(left, right, k):
    if left == right:                                           # 仅含一个元素的数组
        return nums[left]

    location = quickSort(left, right)

    if location == k:
        return nums[location]
    elif location < k:
        return findResult(location+1, right, k)
    elif location > k:
        return findResult(left, location-1, k)

print(findResult(0, len(nums)-1, len(nums) - k))

# 2/2 类版
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#
#         def quickSort(left, right):
#             key = nums[right]  # 本算法中，基准值初始化放在数组尾
#             location = left
#             for i in range(left, right):
#                 if nums[i] < key:
#                     nums[i], nums[location] = nums[location], nums[i]
#                     location = location + 1  # location始终指向大和小的分界点
#             nums[location], nums[right] = nums[right], nums[location]
#             return location  # location即为第x个最小元素
#
#         def findResult(left, right, k):
#             if left == right:  # 仅含一个元素的数组
#                 return nums[left]
#
#             location = quickSort(left, right)
#
#             if location == k:
#                 return nums[location]
#             elif location < k:
#                 return findResult(location + 1, right, k)
#             elif location > k:
#                 return findResult(left, location - 1, k)
#
#         return findResult(0, len(nums) - 1, len(nums) - k)