class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None

    root = Node(data)
    print(f"Enter left child of {data}")
    root.left = create_tree()
    print(f"Enter right child of {data}")
    root.right = create_tree()

    return root

root = create_tree()
print("Binary Tree Created")