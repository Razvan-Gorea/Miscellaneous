# Singlely Linked List

# Define a class for the node
class Node:
    def __init__(self, data):
        self.data = data # Value of Node
        self.next = None # Pointer to next node

# Define the class for the linked list
class LinkedList:
    def __init__(self):
        self.head = None # First node (head) initalized as empty

    def __repr__(self):
        node = self.head # Point to head
        nodes = [] # Storing Nodes
        while node is not None: # If the head exists, add it into the linked list
            nodes.append(str(node.data))
            node = node.next # Point to next node
        nodes.append("None")
        return " -> ".join(nodes)

# Linked List Insertion

class LinkedList:
    # Existing __init__ and __repr__ methods

    def insert_at_beginning(self, data):
        new_node = Node(data) # Create a brand new node
        new_node.next = self.head # New node points to the head of the linked list
        self.head = new_node # The head equals to the new node

    def insert_at_end(self, data):
        new_node = Node(data) # Create a new node
        if self.head is None: # If the head doesn't exist
            self.head = new_node # The new node becomes the head of the linked list
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_node and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            raise IndexError("Index out of range")

# Printing a linked list
class LinkedList:
    # Existing methods

    def print_list(self):
        current_node = self.head
        while current_node: # Start at the head and go through each node, printing the data of each node
            print(current_node.data)
            current_node = current_node.next


# Binary Tree

# Class for a node that belongs to binary tree
class Node:
    def __init__(self, data):
        self.data = data # Value of node
        self.left = None # Pointer to the left child node
        self.right = None # Pointer to the right child node

# Class for the binary tree, using the node class
class BinaryTree:
    def __init__(self):
        self.root = None # Initialize the root as non existant

    def insert(self, data): # Adding a node into the binary tree
        if self.root is None: # if the root doesn't exist
            self.root = Node(data) # The root becomes the new node
        else: # If the root already exists go to the other insert method
            self._insert(data, self.root)

    # If the root exists
    def _insert(self, data, node):
        if data < node.data: # If the data is less than the data found at the root
            if node.left is None: # If the left node doesn't exist
                node.left = Node(data) # Create the left node with the data
            else:
                self._insert(data, node.left) # Else choose the left branch and go one layer down the tree
        else:
            if node.right is None: # If the right node doesn't exist
                node.right = Node(data) # Create the right node with the data
            else:
                self._insert(data, node.right) # Else choose the right branch and go one layer down the tree

    def inorder_traversal(self, node): # Keep choosing the left subtree until no nodes left, then go back up, whilst also viewing all the right nodes of the left subtree, then repeat the process for right subtree
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data)

# Stack (LIFO)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): # Add to the top of the stack (in this case the end)
        self.stack.append(item)

    def pop(self): # Pop the top of the stack (in this case the end)
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self): # Check if stack is empty
        return len(self.stack) == 0

    def size(self): # Method to find the amount of elements in the stack
        return len(self.stack)

    def peek(self): # See the top element of the stack
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

# Queue (FIFO)

# Similar to a stack except you pop first element of the queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) # Pop the first element within the queue
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

