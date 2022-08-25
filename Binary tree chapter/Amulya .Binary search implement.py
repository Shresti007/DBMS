class BST:
    def __init__(self, key):
        self.key = key  # here we are stating it as new node data
        self.left = None  # here it takes left child is none as , it doesnt have any child.
        self.right = None  # here it takes right is None, as it takes

    def insert(self, data):  # here we need to ad new node , in order to add new node ina sequence we need data of
        # it so we are taking it as parameter
        # check empty condition
        # check tree is empty or not.. if empty. node we attach is first node000
        # if not empty , we need to find position of the new attaching node
        if self.key is None:      # if node is empty, but created
            self.key = data       # so value is added to node.
            return
        if self.key == data:      # checking for duplicates.
            return
        if self.key > data:       # data we are going to be added is less than root then it is transfered to
            if self.left:         # it mean if self.left is present then we will insert data in it, else create new node
                self.left.insert(data)  # calling recursively to perform
            else:
                self.left = BST(data)  # insert new node in left if node is not present
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found")
            return                 #
        if data < root.key:
            if self.left:    # we are saying if left child is present
                self.left.search(data)  # we have to call search opearation recursively on left node.
            else:
                print("node is not present in tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not present in tree")
        # here in search method we are not writing code for duplicate values as we have taken insertion operation
        # with out duplicates

    def preorder_traversal(self):
        print(self.key)  # printing the Node
        if self.left:     # it says self.child is present
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left:       # if self.left is present
            self.left.inorder_traversal()
        print(self.key)
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.key)

    def delete(self, data):          # function for except root node with one child
        if self.key is None:         # if root is empty, second finding the node, third step deleting the node.
            print("Tree is empty")
            return
        if data < self.key:           # we are in search of node which we wish to delete
            if self.left:            # if left node is present or not
                self.left = self.left.delete(data)
            else:
                print(" given node is not present in tree")
        elif data > self.key:        # we are in search to find the node to be deleted
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.left is None:     # this condition applies when node have zero or one child
                temp = self.right     # if left child is none then return right.
                self = None
                return temp
            if self.right is None:    # this condition applies when node have zero or one child
                temp = self.left
                self.left = None
                return temp
            node = self.right          # here if u have two child and deleting parent node first  right child will be
                                       # replaced as parent child in place of deleting node
            # if u delete right subtree smallest value for node will be left subtrree which will become root
            while node.left:           # until node.left is none traverse through tree
                node = node.left
                self.key = node.key    # self.key is right key which is replaced from actual parent node
                self.right = self.right.delete(node.key)   # as now right child is empty it gets deleted
            return self

    def min_node(self):
        current = self   # assigning a variable for root node
        while current.left is not None: # can be also represented as while current.left
            current = current.left
        print("node with smallest key is : ", current.key)

    def max_node(self):
        current = self
        while current.right is not None:
            current = current.right
        print("Node with the smallest key is:", current.key)


root = BST(10)  # here actual root node created and its key value which is dat has been initially taken as none.
root.insert(20)  # here we are inserting data for node. if node is none , it takes the value as root key root.data




# root = BST(10)
# LIST1 = [6,3,1,6,98,3,7]
#for i in list1:
#    root.insert(i)
#root.search(60)
#print("preorder")
#root.preorder_traversal()
#print("Inorder")
#root.inorder_traversal()
#print("postorder")
#root.postorder_traversal()
root.delete(6)