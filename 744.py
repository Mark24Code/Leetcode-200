# 输入输出版
letter = input("请输入有序字符数组letters(以逗号隔开）：")      #如：c,f,j
letters = letter.split(",")
target = input("请输入一个目标字符target：")                    #如：a
if letters[len(letters)-1] <= target:
    result = letters[0]
else:
    l = 0
    h = len(letters)-1
    result = ""
    while l <= h:
        mid = l + (h-l)//2
        if letters[mid] > target:
            h = mid - 1
        else:
            l = mid + 1

    result = letters[l]
print(result)

# 类版
# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         """
#         :type letters: List[str]
#         :type target: str
#         :rtype: str
#         """
#         if letters[len(letters)-1] <= target:
#             return letters[0]
#         l = 0
#         h = len(letters)-1
#         result = ""
#         while l <= h:
#             mid = l + (h-l)//2
#             if letters[mid] > target:
#                 h = mid - 1
#             else:
#                 l = mid + 1
#         return letters[l]