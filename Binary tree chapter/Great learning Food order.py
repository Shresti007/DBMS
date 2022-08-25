class Node:
    def __init__(self, price, item_name, quantity):
        self.left = None
        self.right = None
        self.val = price
        self.item_name = item_name
        self.quantity = quantity

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val > node.val:   # comparing the value of root with node val which we want to insert
            if root.left:
                insert(root.left,node)
            else:
                root.left = node
        else:
            if root.right:
                insert(root.right, node)
            else:
                root.right = node

def reverse_inorder_for_greater_values(root, compare_value, result = []):
    if not root:
        return
    reverse_inorder_for_greater_values(root.right, compare_value, result)
    if root.val >= compare_value:
        result.append((root.item_name, root.quantity, root.val))
    reverse_inorder_for_greater_values(root.right, compare_value, result)

def inorder_for_smaller_values(root, compare_value, result = []):
    if not root: return
    inorder_for_smaller_values(root.left, compare_value, result)
    if root.val <= compare_value:
        result.append((root.item_name, root.quantity, root.val))
    inorder_for_smaller_values(root.right, compare_value, result)


if __name__ == "__main__":
    root = Node(30, "Cheese Pizza", 1)
    insert(root, Node(15, "veg Sandwich", 2))
    insert(root, Node(20, "plain Sandwich", 2))
    insert(root, Node(10, "plain Sandwich", 1))
    insert(root, Node(40, "Chicken Burger", 1))
    insert(root, Node(35, "Veg Burger", 1))
    insert(root, Node(45, "Chicken Pizza", 1))

    greater_result = [ ]

    reverse_inorder_for_greater_values(root, 20, greater_result)

    print(greater_result)

    smaller_result = [ ]
    inorder_for_smaller_values(root, 40, smaller_result)
    print(smaller_result)





