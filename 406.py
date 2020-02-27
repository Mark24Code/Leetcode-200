# 输入版
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
def takeSecond(elem):
    return elem[1]

def takeFirst(elem):
    return elem[0]

people.sort(key=takeSecond)
people.sort(key=takeFirst, reverse=True)

result = []
for p in people:
    result.insert(p[1], p)

print(result)

# 类版本
# class Solution(object):
#     def reconstructQueue(self, people):
#         """
#         :type people: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         def takeSecond(elem):
#             return elem[1]
#
#         def takeFirst(elem):
#             return elem[0]
#
#         people.sort(key=takeSecond)
#         people.sort(key=takeFirst, reverse=True)
#
#         result = []
#         for p in people:
#             result.insert(p[1], p)
#         return result