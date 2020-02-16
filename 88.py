# 1/3输入输出版本
num1 = [0]
num2 = [1]
m = 0
n = 1

new = m + n - 1 # 归并后最后一个元素的下标
x = m-1
y = n-1 # x, y双指针

while x >= 0 or y >= 0:
    if x < 0:
        num1[new] = num2[y]

        new = new - 1
        y = y - 1
    elif y < 0:
        num1[new] = num1[x]
        new = new - 1
        x = x - 1
    elif num1[x] <= num2[y]:
        num1[new] = num2[y]
        new = new - 1
        y = y - 1
    else:
        num1[new] = num1[x]
        new = new - 1
        x = x - 1

print(num1)

# 2/3 类版本
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         new = m + n - 1 # 归并后最后一个元素的下标
#         x = m-1
#         y = n-1 # x, y双指针
#
#         while x >= 0 or y >= 0:
#             if x < 0:
#                 nums1[new] = nums2[y]
#                 new = new-1
#                 y = y-1
#             elif y < 0:
#                 nums1[new] = nums1[x]
#                 new = new - 1
#                 x = x - 1
#             elif nums1[x] <= nums2[y]:
#                 nums1[new] = nums2[y]
#                 new = new - 1
#                 y = y - 1
#             else:
#                 nums1[new] = nums1[x]
#                 new = new - 1
#                 x = x - 1

# 3/3 逆天版
#
# num1[m:m+n] = num2      # 将nums2合并到nums1中
# num1.sort()              # 直接使用内置排序方法sort