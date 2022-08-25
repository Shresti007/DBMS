
# A Node class represent each node of tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def balnced_tree(arr, start, end):
    '''A function creates the Balanced Binary Search tree  using sorted array
        |    arr   = parameter takes tha arr
        |    start = it takes the startng index of the given array
        |    end   = takes last index of the array
    '''
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left = balnced_tree(arr, start, mid - 1)
    root.right = balnced_tree(arr, mid + 1, end)
    return root


def inorder(root):
    '''Function to print the tree'''
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = balnced_tree(arr, 0, len(arr) - 1)
    inorder(tree)

