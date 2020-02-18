# 输入输出版
s = input("请输入一个字符串：")
# d = ["ale", "apple", "monkey", "plea"]
# d = ["ba", "ab", "a", "b"]
d1 = input("请输入字符串字典:(以，隔开)")
d = d1.split(",")
print(d)
longestWord = ""

for i in range(0, len(d)):
    target = d[i]
    x = 0
    y = 0
    while x < len(s) and y < len(target):
        if s[x] == target[y]:
            x = x + 1
            y = y + 1
        else:
            x = x + 1
    if y == len(target):
        if len(target) > len(longestWord):
            longestWord = ""
            longestWord = longestWord + target
        if len(target) == len(longestWord) and target < longestWord:
            longestWord = ""
            longestWord = longestWord + target

if len(longestWord) == 0:
    print("")
else:
    print(longestWord)

# 类结构版
# class Solution(object):
#     def findLongestWord(self, s, d):
#         """
#         :type s: str
#         :type d: List[str]
#         :rtype: str
#         """
#         longestWord = ""
#
#         for i in range(0, len(d)):
#             target = d[i]
#             x = 0
#             y = 0
#             while x < len(s) and y < len(target):
#                 if s[x] == target[y]:
#                     x = x + 1
#                     y = y + 1
#                 else:
#                     x = x + 1
#             if y == len(target):
#                 if len(target) > len(longestWord):
#                     longestWord = ""
#                     longestWord = longestWord + target
#                 if len(target) == len(longestWord) and target < longestWord:
#                     longestWord = ""
#                     longestWord = longestWord + target
#         if len(longestWord) == 0:
#             return ""
#         else:
#             return longestWord