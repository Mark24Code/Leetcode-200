# 输入输出版
from collections import Counter
str = input("请输入一个字符串：")

frequence = Counter(str)
F = frequence.most_common(len(frequence))
result = ""

for i in range(0, len(F)):
    for j in range(1, F[i][1]+1):
        result = result + F[i][0]

print(result)

# 类版
# from collections import Counter
# class Solution(object):
#     def frequencySort(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         frequence = Counter(s)
#         F = frequence.most_common(len(frequence))
#         result = ""
#
#         for i in range(0, len(F)):
#             for j in range(1, F[i][1]+1):
#                 result = result + F[i][0]
#         return result