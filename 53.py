# 输出版
nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = nums[0]
cur_sum = nums[0]
for i in range(1, len(nums)):
    if nums[i] > cur_sum + nums[i]:
        cur_sum = nums[i]
    else:
        cur_sum = cur_sum + nums[i]
    if max_sum < cur_sum:
        max_sum = cur_sum

print(max_sum)

# 类版
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_sum = nums[0]
#         cur_sum = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i] > cur_sum + nums[i]:
#                 cur_sum = nums[i]
#             else:
#                 cur_sum = cur_sum + nums[i]
#             if max_sum < cur_sum:
#                 max_sum = cur_sum
#
#         return max_sum