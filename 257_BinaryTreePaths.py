# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def dfs(node, strs, lst):
            if strs:
                strs = strs + '->'
            strs = strs + str(node.val)
            if node.left:
                dfs(node.left, strs, lst)
            if node.right:
                dfs(node.right, strs, lst)
            if not node.right and not node.left:
                lst.append(strs)

        if not root: return []
        lst = []
        strs = ''
        dfs(root, strs, lst)
        return lst


'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
这题尝试了下使用Python的可变对象和不可变对象的特性，在递归中，可变对象在出栈后仍保持不变，不可变对象则会被修改为栈中对应值。
'''