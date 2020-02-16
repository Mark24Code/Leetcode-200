# numbers target于object对象版
# class Solution(object):
# #     def twoSum(self, numbers, target):
# #         """
# #         :type numbers: List[int]
# #         :type target: int
# #         :rtype: List[int]
# #         """
# #         i = 0
# #         j = len(numbers)-1
# #         while i < j:
# #             if numbers[i] + numbers[j] == target:
# #                 return [i+1, j+1]
# #                 break
# #             elif numbers[i] + numbers[j] < target:
# #                 i = i+1
# #             elif numbers[i] + numbers[j] > target:
# #                 j = j-1

#用户指定numbers target版
number = input("numbers:")
target = input("target:")
numbers = [int(n) for n in number.split( )]
i = 0
j = len(numbers) - 1
while i < j:
    if numbers[i] + numbers[j] == int(target):
        print([i + 1, j + 1])
        break
    elif numbers[i] + numbers[j] < int(target):
        i = i + 1
    elif numbers[i] + numbers[j] > int(target):
        j = j - 1