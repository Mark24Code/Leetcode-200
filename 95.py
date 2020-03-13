# 仅类版
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return generateSubTrees(1,n)

def generateSubTrees(l, h):
    result = []
    if l > h:
        result.append(None)
        return result
    for i in range(l, h+1):
        leftTree = generateSubTrees(l, i-1)
        rightTree = generateSubTrees(i+1, h)
        for le in leftTree:
            for ri in rightTree:
                root = TreeNode(i)
                root.left = le
                root.right = ri
                result.append(root)
    return result