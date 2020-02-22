# 输入输出版
from collections import Counter
nums = [1, 1, 1, 2, 2, 3]
k = 2

frequence = Counter(nums).most_common(k)
print(Counter(nums))
result = []
for i in range(0, k):
    result.append(frequence[i][0])

print(result)

# 类版
# from collections import Counter
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#
#         frequence = Counter(nums).most_common(k)
#         result = []
#         for i in range(0, k):
#             result.append(frequence[i][0])
#
#         return result