import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def display(self, current, level=0):
        if current is not None:
            self.display(current.right, level + 1)
            print(' ' * 4 * level + '->', current.value)
            self.display(current.left, level + 1)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.value, end=' ')
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=' ')


# set1
set1 = ["Mick", "Ringo", "George", "Paul", "John", "Jackson", 'Dylon', 'Hendrix', 'ZZTop', 'Page']
bst1 = BST()
for value in set1:
    bst1.insert(value)

# set2
set2 = random.sample(range(45), 10)
bst2 = BST()
for value in set2:
    bst2.insert(value)

# Display BST1
print('--- BST1 ---')
print('Original list:', set1)
bst1.display(bst1.root)
print('In-order traversal:', end=' ')
bst1.in_order(bst1.root)
print()
print('Pre-order traversal:', end=' ')
bst1.pre_order(bst1.root)
print()
print('Post-order traversal:', end=' ')
bst1.post_order(bst1.root)
print()

# Display BST2
print('--- BST2 ---')
print('Original list:', set2)
bst2.display(bst2.root)
print('In-order traversal:', end=' ')
bst2.in_order(bst2.root)
print()
print('Pre-order traversal:', end=' ')
bst2.pre_order(bst2.root)
print()
print('Post-order traversal:', end=' ')
bst2.post_order(bst2.root)
print()

"""
Results:
--- BST1 ---
Original list: ['Mick', 'Ringo', 'George', 'Paul', 'John', 'Jackson', 'Dylon', 'Hendrix', 'ZZTop', 'Page']
        -> ZZTop
    -> Ringo
        -> Paul
            -> Page
-> Mick
        -> John
            -> Jackson
                -> Hendrix
    -> George
        -> Dylon
In-order traversal: Dylon George Hendrix Jackson John Mick Page Paul Ringo ZZTop 
Pre-order traversal: Mick George Dylon John Jackson Hendrix Ringo Paul Page ZZTop 
Post-order traversal: Dylon Hendrix Jackson John George Page Paul ZZTop Ringo Mick 
--- BST2 ---
Original list: [6, 14, 66, 55, 30, 10, 94, 15, 61, 25]
            -> 94
        -> 66
                -> 61
            -> 55
                -> 30
                        -> 25
                    -> 15
    -> 14
        -> 10
-> 6
In-order traversal: 6 10 14 15 25 30 55 61 66 94 
Pre-order traversal: 6 14 10 66 55 30 15 25 61 94 
Post-order traversal: 10 25 15 30 61 55 94 66 14 6 

Process finished with exit code 0

"""