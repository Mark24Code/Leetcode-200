# 输入输出版
s = input("请输入一个需要查找的子序列s：")
t = input("请输入一个长字符串t：")

i = 0
j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i = i + 1
        j = j + 1
    else:
        j = j + 1

if i == len(s):
    print(True)
else:
    print(False)

# 类版
# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         i = 0
#         j = 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i = i + 1
#                 j = j + 1
#             else:
#                 j = j + 1
#
#         if i == len(s):
#             return True
#         else:
#             return False