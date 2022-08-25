class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return -1

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None                                                   # while Tree is not empty
        node = self.root # data searching is not in root Node so we assume node in which data will be taken root node.

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild  # del n left becomes par left
            else:
                parent.rightChild = node.leftChild   # here it mean del n is right to par, del n left is now par child
            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild # here del n is rt to par, del n child is right to del n, so aft del
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node        #
            delNode = node.rightChild   # WE HAVE FIND DEL NODE with lower val IN RIGHT SUB TREE OF ACTUAL DELETING NODE
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value # now actual deleting node value is replaced by lowest key del node val
            if delNode.rightChild:     # if del node has right child as anyway it is the only left smal key prst in tre
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild  # so here if del node has r, this r becom l of del par
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild # so here del r bec , r of par in place of del node.
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None    # that mean del node is not having any right kid
                else:
                    delNodeParent.rightChild = None # if del node is right kid and it is deleted so no more to add

    def preorder(self):
        if self.root is not None:
            print("PreOrder", end = '')
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("PostOrder", end = '')
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder", end = '')
            self.root.inorder()


bst = Tree()
print(bst.insert(10))
# print(bst.insert(5))
bst.preorder()
print(bst.getHeight())
# bst.postorder()
# bst.inorder()
print(bst.remove(10))
bst.preorder()

def remove(self, data):
    # empty tree
    if self.root is None:
        return False

    # data is in root node
    elif self.root.value == data:
        if self.root.left is None and self.root.right is None:
            self.root = None
        elif self.root.left and self.root.right is None:
            self.root = self.root.left
        elif self.root.left is None and self.root.right:
            self.root = self.root.right
        elif self.root.left and self.root.right:
            delNodeParent = self.root
            delNode = self.root.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            self.root.value = delNode.value
            if delNode.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNodeParent.value < delNode.value:
                    delNodeParent.right = delNode.right
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None

        return True

    parent = None   # when
    node = self.root

    # find node to remove
    while node and node.value != data:
        parent = node
        if data < node.value:
            node = node.left
        elif data > node.value:
            node = node.right

    # case 1 data not found
    if node is None or node.value != data:
        return False

    # case 2: remove - node has no children
    elif node.left is None and node.right is None:
        if data < parent.value:
            parent.left = None
        else:
            parent.right = None
        return True

    #case 3: remove node has left child only
    elif node.left and node.right is None:  #
        if data < parent.value:             # if removing node.data is left of root node and having only one child @left
            parent.left = node.left         # then parents.left will become removing nodes  only child which is left of it
        else:
            parent.right = node.left  # else if our deleting node is right to its parent node, deleting node child which is left to it now becomes right of deleting nodes parent
        return True

    # case4: remove-node has right child only.
    elif node.left is None and node.right:
        if data < parent.value:     # here root node has one child which is right to it
            parent.left = node.right # if deleting node is left to its parent node and deelting node child is right to it, then deleting node right becomes parentss left
        else:
            parent.right = node.right  # here if we are deleting parents right child and deleting node is having right kid, parents right becoomes deleting node right
        return True

    # case 5: remove-node has left and right children
    else:
        delNodeParent = node   # here if we found deleting node has both childs, then its replacement values delnode
        delNode = node.right
        while delNode.left:
            delNodeParent = delNode
            delNode = delNode.left

        node.value = delNode.value  # here node val has been changed with last min valued node of its right deleting node
        if delNode.right:
            if delNodeParent.left > delNode.value:
                delNodeParent.left = delNode.right
            elif delNodeParent.value < delNode.value:
                delNodeParent.right = delNode.right
        else:
            if delNode.value < delNodeParent.value:
                delNodeParent.left = None
            else:
                delNodeParent.right = None

#def preorder(self):


