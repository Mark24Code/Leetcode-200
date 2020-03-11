# 输入输出版
inp = input("请输入一个整数x：")
x = int(inp)

l = 1
h = x
result = x
while l <= h:
    mid = l + (h-l) // 2
    sqrt = x // mid
    if sqrt == mid:
        result = mid
        break
    elif sqrt < mid:
        h = mid - 1
    elif sqrt > mid:
        l = mid + 1
if result == x:
    result = h
print(result)

# 类版
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         l = 1
#         h = x
#         while l <= h:
#             mid = l + (h - l) // 2
#             sqrt = x // mid
#             if sqrt == mid:
#                 return mid
#             elif sqrt < mid:
#                 h = mid - 1
#             elif sqrt > mid:
#                 l = mid + 1
#
#         return h