# Function to perform inorder traversal on the tree
def inorder(root): # Left -> Root -> Right
    if root is None:
        return
    inorder(root.left)
    print(root.data, end =" ")
    inorder(root.right)

# Pre_order_traversal:
def pre_order(root):  # Root -> Left -> Right

    # if root is None,return
    if root is None:
        return
    # print the current node
    print(root.data, end=" ")
    # traverse left subtree
    pre_order (root.left)

    # traverse right subtree
    pre_order(root.right)
    #


def postorder(root): # Left -> Right -> Root
    # if root is None,return
    if root is None:
        return
    # traverse left subtree
    postorder(root.left)

    # traverse right subtree
    postorder(root.right)
    # print the current node
    print(root.data, end=" ")

# **********  f.   add code to return a post_Order list [ ]


def postorder_hlp(rt):
    ls = []
    postorder_ls(rt, ls)
    return ls
def postorder_ls(root, ls):
    # if root is None,return
    if root is None:
        return ls

    # f...... ********* add codes here
def new_postorder(ls):
    if ls is None:
        return []
    left_list = new_postorder(ls.left)
    right_list = new_postorder(ls.right)
    return left_list + right_list + [ls.data]



def minValueNode(node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left
        return current.data


def maxiValueNode(node):
    current = node

    # loop down to find the rightmost leaf
    while (current.right is not None):
        current = current.right
    return current.data





#       return current.data


'''
# Function to trim the BST and remove nodes having keys outside the valid range

- move the root (recursively) to the smallest node (root.left)
    check if the root.data is less than the lower boundary
        if yes, update the root to root.right
    It will stop (updating) when lower boundary is met

- move the root (recursively) to the largest node (root.right)
    check if the root.data is larger than the upper boundary
        if yes, update the root to root.left
    It will stop (updating) when upprt boundary is met


'''

def trim(root, low, high):
    if not root:
        return None

    # Traverse left subtree
    root.left = trim(root.left, low, high)

    # Traverse right subtree
    root.right = trim(root.right, low, high)

    # Check if the node's data is outside the minimum-maximum boundary
    if root.data < low:
        return root.right

    if root.data > high:
        return root.left

    # Return the root node if it is within the minimum-maximum boundary
    return root

