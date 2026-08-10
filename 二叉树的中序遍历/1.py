# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):

        tree=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)
        dfs(root)
        return tree