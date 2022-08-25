class BinaryNode:

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def createNode(self, key):
        return BinaryNode(key, None, None)

    def insert(self, key, parent, direction):
        curr = self.createNode(key)            # her we are creating the node
        if direction == "left":                # here based on direction we insert child nodes to curr node
            parent.left = curr                 # inserting child node to left of parent node
        else:
            parent.right = curr                # inserting child node to right of parent node
        return curr                            #

    def inorder(self, root):
        if root is None:              # inorder to traverse first checking base con whetr tree is with nodes r not.
            return                    # break adn return if tree is empty
        self.inorder(root.left)       # else traverse through first node
        print(root.data, end=" ")     # traverse through parent node
        self.inorder(root.right)      # traverse through right node

    def preorder(self, root):
        if root is None:              # base condition check, is tree empty or not.
            return                    # return if it is empty
        print(root.data, end=" ")     # travere first through parent node.
        self.preorder(root.left)      # traverse through child node.
        self.preorder(root.right)     # traverse through right child node

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")



tree = BinaryTree()
root = BinaryNode(100, None, None)
rootLeft = tree.insert(50, root, "left")
rootRight = tree.insert(10, root, "right")
rootLeftLeft = tree.insert(70, rootLeft, "left")
# pic of above diagram
'''
                    100
                50          10
            70      

'''
print("Inorder: ")  # 70, 50, 100, 10,
tree.inorder(root)
print("\nPreorder: ")  # 100, 50, 70,10
tree.preorder(root)
print("\nPostorder: ")  # 70,50,10,100
tree.postorder(root)
