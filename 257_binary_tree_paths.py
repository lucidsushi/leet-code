from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(self, root: TreeNode) -> List[str]:

    paths = []

    def dfs(root, path):

        if root.left:
            dfs(root.left, f"{path}->{str(root.left.val)}")
        if root.right:
            dfs(root.right, f"{path}->{str(root.right.val)}")
        if not root.left and not root.right:
            paths.append(path)

        return paths

    return dfs(root, str(root.val)) if root else paths


def build_tree():
    pass


assert binaryTreePaths([1, 2, 3, None, 5]) == ["1->2->5", "1->3"]
