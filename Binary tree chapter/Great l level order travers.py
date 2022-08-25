class BinaryNode:

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def createNode(self, key):
        return BinaryNode(key, None, None)

    def insert(self, key, parent, direction):
        curr = self.createNode(key)      #
        if direction == "left":
            parent.left = curr
        else:
            parent.right = curr
        return curr

    def levelOrder(self, root):
        if root is None:   # checking condition whether it is full or not
            return
        queue = []
        queue.append(root)   # first we needd to append the root in to queue
        while len(queue) > 0:  # checking base condition for while loop
            node = queue.pop(0)   # pop the root element from empty queue and check if it have any child nodes
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            print(node.data)        # after pop print the root and append each child

    def levelOrderSearch(self, root, key):
        if root is None:
            return None
        queue = []
        if root.data == key:
            return root
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.data == key:
                return None
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return None



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
tree.levelOrder(root)
print("LevelOrder: ")  # 70, 50, 100, 10,

# space complexity : o(n)  as it is qeueue tmp is been created
# time complexity: o(n)

