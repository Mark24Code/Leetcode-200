# 输出版
prices = [7,6,4,3,1]

totalEarn = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        totalEarn = totalEarn + (prices[i] - prices[i-1])

print(totalEarn)

# 类版
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         totalEarn = 0
#
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 totalEarn = totalEarn + (prices[i] - prices[i-1])
#
#         return totalEarn