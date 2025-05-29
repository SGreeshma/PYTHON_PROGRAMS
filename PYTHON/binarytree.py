class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def create_btree(arr, i, n):
    if i > n:  
        return None
    root = TreeNode(arr[i - 1])
    root.left = create_btree(arr, 2 * i, n)
    root.right = create_btree(arr, 2 * i + 1, n)
    return root

def preorder(root):
    if root is None:  
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

def levelorder(root):
    if root is None:
        return
    result=[]
    queue=[root]
    while queue:
        node=queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

arr = [3, 4, 5, 6, 7, 8, 9, 0]
bt = create_btree(arr, 1, len(arr))
print("Preorder:")
preorder(bt)
print("\nInorder:")
inorder(bt)
print("\nPostorder:")
postorder(bt)
print("\nLevelorder:")
print(levelorder(bt))