# 输出版
points = [[10, 16], [2, 8], [1, 6], [7, 12]]

def takeSecond(elem):
    return elem[1]

if len(points) == 0:
    print(0)
else:
    points.sort(key=takeSecond)

    i = 0
    count = 1
    last = points[0]

    while i < len(points):
        if points[i][0] <= last[1]:
            i = i + 1
        else:
            count = count + 1
            last = points[i]
            i = i + 1

    print(count)

# 类版
# class Solution(object):
#     def findMinArrowShots(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         if len(points) == 0:
#             return 0
#         def takeSecond(elem):
#             return elem[1]
#
#         points.sort(key=takeSecond)
#
#         i = 0
#         count = 1
#         last = points[0]
#
#         while i < len(points):
#             if points[i][0] <= last[1]:
#                 i = i + 1
#             else:
#                 count = count + 1
#                 last = points[i]
#                 i = i + 1
#         return count