# finding height of tree
def findheight(root):
    if root is None:
        return -1
    left_height = findheight(root.left)
    right_height = findheight(root.right)

    return max(left_height,right_height)+1


