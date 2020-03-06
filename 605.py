# 输入输出版
flowerbed = [1,0,0,0,1]
n = 2

count = 0

for i in range(0, len(flowerbed)):
    if flowerbed[i] == 0:
        if len(flowerbed) > 1:
            if i == 0:
                if flowerbed[i+1] != 1:
                    count = count + 1
                    flowerbed[i] = 1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] != 1:
                    count = count + 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    count = count + 1
                    flowerbed[i] = 1
        else:
            count = count + 1

if count >= n:
    print(True)
else:
    print(False)


# 类版
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         count = 0
#
#         for i in range(0, len(flowerbed)):
#             if flowerbed[i] == 0:
#                 if len(flowerbed) > 1:
#                     if i == 0:
#                         if flowerbed[i + 1] != 1:
#                             count = count + 1
#                             flowerbed[i] = 1
#                     elif i == len(flowerbed) - 1:
#                         if flowerbed[i - 1] != 1:
#                             count = count + 1
#                             flowerbed[i] = 1
#                     else:
#                         if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
#                             count = count + 1
#                             flowerbed[i] = 1
#                 else:
#                     count = count + 1
#                     flowerbed[i] = 1
#
#         return count >= n