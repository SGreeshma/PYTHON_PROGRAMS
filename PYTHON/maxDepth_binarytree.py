#maxDepth of binary tree with recursion

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    leftD=maxDepth(root.left)
    rightD=maxDepth(root.right)
    res=1+max(leftD, rightD) # 1 is used to include root node
    return res

if __name__=="__main__":
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(10)
    root.left.left=TreeNode(8)
    root.left.left.left=TreeNode(7)
    print(maxDepth(root))
