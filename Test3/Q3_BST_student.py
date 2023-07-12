"""
The inorder, insert(..) methods are defined outside to BST_Node Class

"""
import sys

from randomNumLst import ranGen
from BST_util_student import *


# A class to store a BST node
class BST_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # self.count = 0

    def insert(self, data):
        if data == self.data:  # skip (return) if new data exist already in the tree
            return
        # Recursively call the insert method to add the data to the leaf
        if data < self.data:
            # Add to left subtree
            if self.left:  # keep calling insert(data) until none (leaf)
                self.left.insert(data)
            else:  # at leaf add the BST_Node(data)
                self.left = BST_Node(data)
        # Recursively call the insert method to add the data to the leaf
        else:
            # Add to right subtree
            if self.right:  # keep calling insert(data) until none (leaf)
                self.right.insert(data)
            else:
                self.right = BST_Node(data)

    def search_element(self, elem, count, path=""):  # complexity of O(log n)
        count += 1
        if self is None:
            return -1, count + 1
        if self.data == elem:
            print(f'{count}, {path}')
            return
        elif elem < self.data:
            if self.left:
                self.left.search_element(elem, count, path + "left, ")
            else:
                print(f'cannot find-left {elem} at {count}')
                return False
        else:
            if self.right:
                self.right.search_element(elem, count, path + "right, ")
            else:
                print(f'cannot find-right {elem} at {count}')
                return False


    def deleteNode(self, rt, key):
        # Base Case
        if rt is None:
            return rt

        # If the key to be deleted is smaller than the root's key then it is in  left subtree
        if key < rt.data:
            rt.left = rt.deleteNode(rt.left, key)

        # If the data to be delete # is greater than the root's data then it lies in right (successor) subtree

        elif (key > rt.data):
            rt.right = rt.deleteNode(rt.right, key)

        # If key is same as root's key, then this is the root node to be deleted
        else:
            # BST_Node with only one child or no child
            if rt.left is None:
                temp = rt.right
                rt = None
                return temp

            elif rt.right is None:
                temp = rt.left
                rt = None
                return temp

            # BST_Node with two children: Get the smallest of successor (smallest in the right subtree)
            temp = minValueNode(rt.right)  # note temp is NOT a BST_Node, it is a data (value)

            # Copy the inorder successor's data (temp) to this node
            rt.data = temp

            # Delete the inorder successor
            rt.right = rt.deleteNode(rt.right, temp)

        return rt

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def lst_to_BST(lst_elem):
    if len(lst_elem) > 1:
        # start with ls[0] as root
        root_node = BST_Node(lst_elem[0])

        for x in lst_elem:
            root_node.insert(x)
        return root_node
    else:
        return print("Insufficient number of elements")


if __name__ == '__main__':

    # a. create and display three BST trees back on the following two list plus a random number list of 30 elements

    set1 = ["Michael", "Ringo", "George", "Paul", "John", "Jackson", 'Dylon', 'Hendrix', 'ZZTop', 'Page']

    set2 = ranGen(45)

    runX = 0
    set_used = set1
    b1 = lst_to_BST(set_used)

    # ************** remove the above four lines of codes after you get the following working _************

    # ************  a. (0, 1) add your codes here to loop thru the two lists *********

    b1 = BST_Node(set1[0])
    for i in range(1, len(set1)):
        b1.insert(set1[i])

    # Display the BST tree and the original list for set1
    print('\n --- A.0 BST tree from a list of names')
    print("BST tree for set1:")
    b1.display()
    print("\nOriginal list for set1:")
    print(set1)

    # Print in-order, pre-order, and post-order traversals for bst1
    print("\nIn-order traversal for set1:")
    inorder(b1)
    print("\nPre-order traversal for set1:")
    pre_order(b1)
    print("\nPost-order traversal for set1:")
    postorder(b1)

    # Convert set2 to a BST tree
    b1 = BST_Node(set2[0])
    for i in range(1, len(set2)):
        b1.insert(set2[i])

    # Display the BST tree and the original list for set2
    print("\n\n --- A.1 BST tree from a list of 45 random numbers")
    print("BST tree for set2:")
    b1.display()
    print("\nOriginal list for set2:")
    print(set2)

    # Print in-order, pre-order, and post-order traversals for bst2
    print("\nIn-order traversal for set2:")
    inorder(b1)
    print("\nPre-order traversal for set2:")
    pre_order(b1)
    print("\nPost-order traversal for set2:")
    postorder(b1)

    # print ("Out of runX !")

# b write a maxiValueNode(node) function in the the BST_Util.py module to find
max1 = maxiValueNode(b1)  # *****  need to add codes in BST_util_student.py
print('\n\n --- B. max is ', max1)

# c. Print the search path for finding the int(maximum/2)

#    look = int(max1 / 2)     # ********* need the results from b.

look = int(max1 / 2)
print(f'\n --- C. search path for the maximum/2 "{look}" is: ')
b1.search_element(look, count=0)


# d. Delete the root node and display the BST
print(f"\n ---D. BST after deleting root.data '{b1.data}' from the BST tree")
# **************  add code to remove the root node)

b1.display()

# e. trim the tree with a boundary (min+5, max+5)  # ***** need to modify the trim codes in BST_Util_student
min1 = minValueNode(b1)
print('min is ', min1)

low = min1 + 5
high = max1 - 5
print(f'\n ---E.  trim the BST with low: {low}, and high: {high}')
new_BST = trim(b1, low, high)  # ***** need to modify trim in BST_util_student ********
new_BST.display()

# f.  generated a list[ ] from the post_order functions

print(f'\n ---F.print from the postorder function:')
postorder(b1)

# ****************  add code here to call the new postorder function that returns list[ ] in BST_Util_student.py

# call the new postorder function
ls = new_postorder(b1)

# print the resulting list
print(f'\nlist from the postorder is:\n {ls}')
