def bst_search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return bst_search(root.left, key)
    return bst_search(root.right, key)