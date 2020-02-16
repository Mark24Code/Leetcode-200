# 输入输出版
aeiou = ['a', 'e', 'i', 'o', 'u']
s = input("请输入一个单词：")
output = list(s)
x = 0
y = len(s)-1
while x < y:
    if s[x] in aeiou:
        if s[y] in aeiou:
            output[x] = s[y]
            output[y] = s[x]
            x = x+1
            y = y-1
        else:
            output[y] = s[y]
            y = y-1
    elif s[y] in aeiou:
        output[x] = s[x]
        x = x+1
    else:
        output[x] = s[x]
        output[y] = s[y]
        y = y-1
        x = x+1

j = "".join(output)
print(j)

# 类版
# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         aeiou = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         output = list(s)
#         x = 0
#         y = len(s)-1
#         while x < y:
#             if s[x] in aeiou:
#                 if s[y] in aeiou:
#                     output[x] = s[y]
#                     output[y] = s[x]
#                     x = x+1
#                     y = y-1
#                 else:
#                     output[y] = s[y]
#                     y = y-1
#             elif s[y] in aeiou:
#                 output[x] = s[x]
#                 x = x+1
#             else:
#                 output[x] = s[x]
#                 output[y] = s[y]
#                 y = y-1
#                 x = x+1
#         j = "".join(output)
#         return j
