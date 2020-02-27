# 输出版
intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]

def takeSecond(elem):
    return elem[1]


if len(intervals) == 0:
    print(0)

intervals.sort(key=takeSecond)           # list.sort(cmp=None, key=None, reverse=False)
i = 1
count = 1
last = intervals[0]

while i < len(intervals):
    if intervals[i][0] < last[1]:
        i = i + 1
    else:
        last = intervals[i]
        count = count + 1
        i = i + 1

print(len(intervals) - count)

# 类版
# class Solution(object):
#     def eraseOverlapIntervals(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         def takeSecond(elem):
#             return elem[1]
#
#         if len(intervals) == 0:
#             return 0
#         intervals.sort(key=takeSecond)           # list.sort(cmp=None, key=None, reverse=False)
#         i = 1
#         count = 1
#         last = intervals[0]
#         while i < len(intervals):
#             if intervals[i][0] < last[1]:
#                 i = i + 1
#             else:
#                 last = intervals[i]
#                 count = count + 1
#                 i = i + 1
#         return len(intervals) - count