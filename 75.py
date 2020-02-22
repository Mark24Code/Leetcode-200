# 输入输出版
Input = input("请输入以0，1，2组成的数组，以逗号隔开：")
nums = [int(n) for n in Input.split(",")]
left = -1
right = len(nums)
i = 0

while i < right:
    if nums[i] == 0:
        left = left + 1
        nums[i], nums[left] = nums[left], nums[i]
        i = i + 1
    elif nums[i] == 2:
        right = right - 1
        nums[i], nums[right] = nums[right], nums[i]
    else:
        i = i + 1

print(nums)

# 类版
# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         left = -1
#         right = len(nums)
#         i = 0
#
#         while i < right:
#             if nums[i] == 0:
#                 left = left + 1
#                 nums[i], nums[left] = nums[left], nums[i]
#                 i = i + 1
#             elif nums[i] == 2:
#                 right = right - 1
#                 nums[i], nums[right] = nums[right], nums[i]
#             else:
#                 i = i + 1