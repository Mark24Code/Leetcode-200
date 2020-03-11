# 输入输出版
num = input("请输入一个有序字符数组：")
nums = num.split(",")

l = 0
h = len(nums)-1
while l < h:
    mid = l + (h-l) // 2
    if mid % 2 != 0:
        mid = mid - 1
    if nums[mid] == nums[mid+1]:
        l = mid+2
    else:
        h = mid

print(nums[l])

# 类版
# class Solution(object):
#     def singleNonDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l = 0
#         h = len(nums)-1
#         while l < h:
#             mid = l + (h-l) // 2
#             if mid % 2 != 0:
#                 mid = mid - 1
#             if nums[mid] == nums[mid+1]:
#                 l = mid+2
#             else:
#                 h = mid
#
#         return nums[l]

