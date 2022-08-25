class BinaryNode:

    def __init__(self, data, left = None, right = None):
        self.key = data
        self.left = left
        self.right = right


class BST:
    root = None    # assuming just class created obj has not been allocated

    def insert(self, root, key):
        if root is None:
            return BinaryNode(key, None, None)         # created new node

        if key < root.data:
            root.left = self.insert(root.left, key)    # then update it in left part of root with key
        else:
            root.right = self.insert(root.right, key)  # else it will updates in right node
        return root                                    # return the updated root

    def inorder(self, root):                            # left, root, right
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def search(self, root, key):
        if root is None:
            return None
        if key == root.data:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def successor(self, root):
        tmp = root.right
        while tmp.left is not None:
            tmp = tmp.left
        return tmp
    # if you are deleting node which have two child, if u r deleting from its right child, bring the smallest from its
    # right child. else if u are deleting from its left child insert maximum from its left child. these is for two child
    def delete(self, root, key):
        if root is None:                                  # check root in none
            return root
        if key < root.data:                               # check if root is less than data
            root.left = self.delete(root.left, key)       # here update root left with deletion opern on left half key
        elif key > root.data:
            root.right = self.delete(root.right, key)     # here update root left with deletion opern on right half key
        else:                                             # both above cond fails and key is = to root. data
            if root.left is None:                         # here is we are not having  left child
                return root.right                         # as we are not having left child we return right kid
            elif root.right is None:
                return root.left

            tmp = self.successor(root) # as we find the root to be dele, we find its succesor to take over place of root
            root.data = tmp.data                         # so now successor becomes new root in place of deleted root
            root.right = self.delete(root.right, tmp.data) #
        return root

tree = BST()
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 7)
tree.root = tree.insert(tree.root, 90)
tree.root = tree.insert(tree.root, 12)
tree.root = tree.insert(tree.root, 32)
tree.root = tree.delete(tree.root, 90)

tree.inorder(tree.root)
result = tree.search(tree.root, 32)
if result is None:
    print("element is not found")
else:
    print("element is found")
