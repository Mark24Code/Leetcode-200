# 输入输出版
S = input("请输入一个字符串S：")
last = {}
for i, element in enumerate(S):
    last[element] = i

result = []
start = j = 0
for i, element in enumerate(S):
    if last[element] > j:
        j = last[element]
    if i == j:
        result.append(i - start + 1)
        start = i + 1

print(result)
# 类版
# class Solution(object):
#     def partitionLabels(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#         last = {}
#         for i, element in enumerate(S):
#             last[element] = i
#
#         result = []
#         start = j = 0
#         for i, element in enumerate(S):
#             if last[element] > j:
#                 j = last[element]
#             if i == j:
#                 result.append(i - start + 1)
#                 start = i + 1
#         return result