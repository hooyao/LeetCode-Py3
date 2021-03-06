import sys

from BTreeUtils import BTreeHelper
from BTreeUtils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current_node = root
        while current_node:
            if val == current_node.val:
                return current_node
            elif current_node.val > val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None


def main(*args):
    tree_array = [1, 0]
    root = BTreeHelper.list_to_tree(tree_array)
    val = 1
    result = Solution().searchBST(root, val)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
