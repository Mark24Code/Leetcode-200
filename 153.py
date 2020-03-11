# 输入输出
num = input("请输入一个升序数组旋转后的数组：")
nums = num.split(",")

l = 0
h = len(nums)-1

while l < h:
    mid = l +(h-l)//2
    if nums[mid] <= nums[h]:
        h = mid
    else:
        l = mid + 1

print(nums[l])

# 类版
# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l = 0
#         h = len(nums)-1
#
#         while l < h:
#             mid = l +(h-l)//2
#             if nums[mid] <= nums[h]:
#                 h = mid
#             else:
#                 l = mid + 1
#         return nums[l]