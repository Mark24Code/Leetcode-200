# 输出版
nums = [4,2,1]

count = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1] and nums[i] < nums[i-2] and i-2 >= 0:
        nums[i] = nums[i-1]
        count = count + 1
    elif nums[i] < nums[i-1] and i-1 >= 0:
        nums[i-1] = nums[i]
        count = count + 1

if count > 1:
    print(False)
else:
    print(True)

# 类版
# class Solution(object):
#     def checkPossibility(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         count = 0
#         for i in range(1, len(nums)):
#             if nums[i] < nums[i-1] and nums[i] < nums[i-2] and i-2 >= 0:
#                 nums[i] = nums[i-1]
#                 count = count + 1
#             elif nums[i] < nums[i-1]:
#                 nums[i-1] = nums[i]
#                 count = count + 1
#
#         if count > 1:
#             return False
#         else:
#             return True
