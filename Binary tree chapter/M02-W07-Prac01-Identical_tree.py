# class Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def identicalTrees(root1, root2):
    # pseudocode
    # If there is no element in both the trees, then return true.
    # If both trees have the element, then check for equality and call for left and right subtree.
    # If one tree has an element and the other doesn't then return false.
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return (root1.data == root2.data) and identicalTrees(root1.left, root2.left) and \
               identicalTrees(root1.right, root2.right)
    return False


# main of Sample Test case - 1
# Change this main based on the other test cases
# For other test cases assign new values in roots and subsequently assign values
# to left and right child. 
root1 = Node(34)
root1.left = Node(11)
root1.right = Node(39)
root2 = Node(34)
root2.left = Node(11)
root2.right = Node(39)

# Do not make any changes in this part.
# Name root of your trees as root1 and root2 respectively. 
if identicalTrees(root1, root2):
    print("Identical")
else:
    print("Not Identical")
