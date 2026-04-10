def search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    return search(root.left, key) or search(root.right, key)