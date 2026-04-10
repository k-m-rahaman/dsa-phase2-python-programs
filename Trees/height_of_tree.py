def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1