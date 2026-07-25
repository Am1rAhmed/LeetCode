# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


# Correct solution for LeetCode 105
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root

# S = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
# print(S)


# Function that can be used to print result
def printTree(root):
    if root is None:
        return

    print(root.val)

    printTree(root.left)
    printTree(root.right)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

S = Solution()
root = S.buildTree(preorder, inorder)

printTree(root)

