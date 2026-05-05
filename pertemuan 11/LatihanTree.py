class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)
        return self.root

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
        return parent_node.left

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
        return parent_node.right


tree = BinaryTree()

F = tree.insert_root("F")

B = tree.insert_left(F, "B")
G = tree.insert_right(F, "G")

A = tree.insert_left(B, "A")
D = tree.insert_right(B, "D")

I = tree.insert_right(G, "I")

C = tree.insert_left(D, "C")
E = tree.insert_right(D, "E")

H = tree.insert_left(I, "H")


# Traversal
def preorder(node):
    if node is not None:
        return [node.data] + preorder(node.left) + preorder(node.right)
    return []

def inorder(node):
    if node is not None:
        return inorder(node.left) + [node.data] + inorder(node.right)
    return []

def postorder(node):
    if node is not None:
        return postorder(node.left) + postorder(node.right) + [node.data]
    return []


print("Preorder :", " ".join(preorder(tree.root)))
print("Inorder  :", " ".join(inorder(tree.root)))
print("Postorder:", " ".join(postorder(tree.root)))





