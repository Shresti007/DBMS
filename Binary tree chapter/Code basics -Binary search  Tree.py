class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:   # data about to add is less than current node data
            # add data in left subtree
            if self.left:      # if it has a child node which mean it not a leaf node
                self.left.add_child(data)    # in that case it cal herself again n again recursively using def method
            else:
                # if it is a leaf case and left  subtree is empty
                self.left = BinarySearchTreeNode(data)

        else:

            # add ata in right Node
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):   # left, root, right it visits
        tmp = [ ]
        # visit left tree
        if self.left:
            tmp += self.left.in_order_traversal()  # recurisvely cal it fucntions
        # visit base node
        tmp.append(self.data)

            # visit right tree
        if self.right:
            tmp += self.right.in_order_traversal()
        return tmp

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else: return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):    # for right node deletion
        if val < self.data:
            if self.left:
                self.left.delete(val)   # recursively cal the delete function to find value in left sub tree
                # not taking else part because python by default print if value is not in left not present as None
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None                        # as if we are at last data point
            if self.left is None:
                return self.right                  # deleting the required node
            if self.right is None:
                return self.right

            min_val = self.right.find_min()      # AS WE WANT TO DELETE NODE FROM right sub tree
            self.data = min_val                  # now we are asuuming the val we find is put in current node
            self.right = self.right.delete(min_val)  # deleting the duplicate val

        return self

    def delete(self, val):    # for left    node deletion
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            max_val = self.right.find_min()
            self.data = max_val
            self.right = self.right.delete(max_val)

        return self



def build_tree(tmp):
    root = BinarySearchTreeNode(Binary_Numbers[0])
    for i in range (1, len(Binary_Numbers)):
        root.add_child(Binary_Numbers[i])

    return root

if __name__ == '__main__':
    Binary_Numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    Binary_tree = build_tree(Binary_Numbers)
    print(Binary_tree.in_order_traversal())
    print(Binary_tree.search(4))
    Binary_tree.delete(20)
    print("After deleting 20", Binary_tree.in_order_traversal() )