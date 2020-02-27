# 输入输出版
g1 = input("请输入一个数组表示满足度（以，间隔）：")
s1 = input("请输入一个数组表示饼干大小（以，间隔）：")

g = [int(n) for n in g1.split(",")]
s = [int(m) for m in s1.split(",")]

g.sort()
s.sort()

i = 0
j = 0
count = 0

while i < len(g) and j < len(s):
    if g[i] <= s[j]:
        i = i + 1
        j = j + 1
        count = count + 1
    else:
        j = j + 1

print(count)

# 类版
# class Solution(object):
#     def findContentChildren(self, g, s):
#         """
#         :type g: List[int]
#         :type s: List[int]
#         :rtype: int
#         """
#         g.sort()
#         s.sort()
#
#         i = 0
#         j = 0
#         count = 0
#
#         while i < len(g) and j < len(s):
#             if g[i] <= s[j]:
#                 i = i + 1
#                 j = j + 1
#                 count = count + 1
#             else:
#                 j = j + 1
#         return count
