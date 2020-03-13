# 输入输出版
def diffWaysToCompute(input):
    if input.isdigit():
        return [int(input)]

    result = []
    for i in range(0, len(input)):
        if input[i] == "-" or input[i] == "+" or input[i] == "*":
            left = diffWaysToCompute(input[:i])
            right = diffWaysToCompute(input[i+1:])
            for l in left:
                for r in right:
                    if input[i] == "-":
                        result.append(l-r)
                    elif input[i] == "+":
                        result.append(l+r)
                    elif input[i] == "*":
                        result.append(l*r)
    return result

input = input("请输入一个含-，+，*的运算式：")
print(sorted(diffWaysToCompute(input)))

# 类版
# class Solution(object):
#     def diffWaysToCompute(self, input):
#         """
#         :type input: str
#         :rtype: List[int]
#         """
#         if input.isdigit():
#             return [int(input)]
#
#         result = []
#         for i in range(0, len(input)):
#             if input[i] == "-" or input[i] == "+" or input[i] == "*":
#                 left = self.diffWaysToCompute(input[:i])
#                 right = self.diffWaysToCompute(input[i+1:])
#                 for l in left:
#                     for r in right:
#                         if input[i] == "-":
#                             result.append(l-r)
#                         elif input[i] == "+":
#                             result.append(l+r)
#                         elif input[i] == "*":
#                             result.append(l*r)
#         return sorted(result)