# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# 由于需要调用API：isBadVersion所以没有单机解法

# class Solution(object):
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         l = 0
#         h = n-1
#         while l <= h:
#             mid = l + (h-l)//2
#             if isBadVersion(mid):
#                 h = mid - 1
#             else:
#                 l = mid + 1
#
#         return l