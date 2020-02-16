#输入输出版
import math
c = int(input())
x = 0
y = math.ceil(math.sqrt(c))

if c < 0:
    print("False")
else:
    while x <= y:
        if x*x + y*y == c:
            print("True")
            break
        elif x*x + y*y < c:
            x = x+1
        elif x*x + y*y > c:
            y = y-1

    if x > y:
        print("False")

#类函数版
# import math
# class Solution(object):
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#         x = 0
#         y = math.ceil(math.sqrt(c))
#
#         if c < 0:
#             return False
#         else:
#             while x <= y:
#                 if x*x + y*y == c:
#                     return True
#                 elif x*x + y*y < c:
#                     x = x+1
#                 elif x*x + y*y > c:
#                     y = y-1
#
#             if x > y:
#                 return False