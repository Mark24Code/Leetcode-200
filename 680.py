#输入输出版
def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    x = 0
    y = len(s)-1
    while x < y:
        if s[x] != s[y]:
            # temp1 = ""
            # for i in range(x+1, y+1):
            #     temp1 = temp1 + s[i]
            # temp2 = ""
            # for i in range(x, y):
            #     temp2 = temp2 + s[i]
            return isPalindrome(s[x+1: y+1]) | isPalindrome(s[x:y])
        else:
            x = x+1
            y = y-1

    return True

def isPalindrome(t):
    x = 0
    y = len(t) - 1
    while x < y:
        if t[x] != t[y]:
            return False
        else:
            x = x+1
            y = y-1
    return True

print(validPalindrome(input("请输入：")))

# Leetcode提交版
# class Solution(object):
#     def validPalindrome(self,s):
#         x = 0
#         y = len(s)-1
#         while x < y:
#             if s[x] != s[y]:
#                 return isPalindrome(s[x+1: y+1]) | isPalindrome(s[x:y])
#             else:
#                 x = x+1
#                 y = y-1
#
#         return True
#
# def isPalindrome(t):
#     x = 0
#     y = len(t) - 1
#     while x < y:
#         if t[x] != t[y]:
#             return False
#         else:
#             x = x+1
#             y = y-1
#     return True