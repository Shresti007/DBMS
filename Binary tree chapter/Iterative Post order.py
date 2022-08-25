# https://www.geeksforgeeks.org/print-postorder-from-given-inorder-and-preorder-traversals/?ref=lbp
# Python3 program to print postorder
# traversal from preorder and inorder
# traversals

# A utility function to search x in
# arr[] of size n
def search(arr, x, n):
    for i in range(n):
        if (arr[i] == x):
            return i

    return -1


# Prints postorder traversal from
# given inorder and preorder traversals
def printPostOrder(In, pre, n):
    # The first element in pre[] is always
    # root, search it in in[] to find left
    # and right subtrees
    root = search(In, pre[0], n)

    # If left subtree is not empty,
    # print left subtree
    if (root != 0):
        printPostOrder(In, pre[1:n], root)

    # If right subtree is not empty,
    # print right subtree
    if (root != n - 1):
        printPostOrder(In[root + 1: n],
                       pre[root + 1: n],
                       n - root - 1)

    # Print root
    print(pre[0], end=" ")


# Driver code
In = [4, 2, 5, 1, 3, 6]
pre = [1, 2, 4, 5, 3, 6]
n = len(In)

print("Postorder traversal ")

printPostOrder(In, pre, n)

# This code is contributed by avanitrachhadiya2155
""
https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
""
# Python3 program for iterative postorder traversal
# using one stack

# Stores the answer
ans = []


# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

# https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
'''
1.1 Create an empty stack
2.1 Do following while root is not NULL
    a) Push root's right child and then root to stack.
    b) Set root as root's left child.
2.2 Pop an item from stack and set it as root.
    a) If the popped item has a right child and the right child 
       is at top of stack, then remove the right child from stack,
       push the root back and set root as root's right child.
    b) Else print root's data and set root as NULL.
2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

'''
# A iterative function to do postorder traversal of
# a given binary tree
def postOrderIterative(root):
    # Check for empty tree
    if root is None:
        return

    stack = []

    while (True):

        while (root):
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            # Set root as root's left child
            root = root.left

        # Pop an item from stack and set it as root
        root = stack.pop()

        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
                peek(stack) == root.right):
            stack.pop()  # Remove right child from stack
            stack.append(root)  # Push root back to stack
            root = root.right  # change root so that the
        # righ childis processed next

        # Else print root's data and set root as None
        else:
            ans.append(root.data)
            root = None

        if (len(stack) <= 0):
            break


# Driver pogram to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Post Order traversal of binary tree is")
postOrderIterative(root)
print(ans)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
