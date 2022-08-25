# class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    # Pseudocode
    # Take an empty stack.
    # Push the element, then call on its left child.
    # When the left child becomes null and the stack is not empty, pop and print the element.
    # Now call on popped elements right child and move to the second step.
    stack = root = []
	while stack:
		if node:   # it mean if node in which it is been is it node or not, if not none it goes to else part
			stack.append(data)  # if curr is not none , it comes directly to here and added to stack
			curr = curr.left
		else:
		 	node = stack.pop()
			print(root.data)
			curr = curr.right
		else:


# main of Sample Test case - 1
# Change this main based on the other test cases
# For other test cases assign new values in roots and subsequently assign values
# to left and right child. 

root = Node(34)
root.left = Node(11)
root.right = Node(39)

# Do not make any changes in this part. 
# Function call for inorder. 
inOrder(root)
