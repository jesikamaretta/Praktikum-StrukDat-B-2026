class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # 1. INSERT MANUAL (sesuai skenario)
    def insert_manual(self):
        print("[INFO] Membangun Struktur Gudang...")

        self.root = Node("A")

        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")

        print("[INFO] Struktur berhasil dibuat.")

    # 2. PREORDER
    def preorder(self, node):
        if node is not None:
            return [node.data] + self.preorder(node.left) + self.preorder(node.right)
        return []

    # 3. INORDER
    def inorder(self, node):
        if node is not None:
            return self.inorder(node.left) + [node.data] + self.inorder(node.right)
        return []

    # 4. POSTORDER
    def postorder(self, node):
        if node is not None:
            return self.postorder(node.left) + self.postorder(node.right) + [node.data]
        return []

    # 5. LEAF NODES
    def get_leaf_nodes(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.data]
        return self.get_leaf_nodes(node.left) + self.get_leaf_nodes(node.right)




tree = BinaryTree()
print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("======================================")

tree.insert_manual()

print("\nHASIL AUDIT:")

print("1. Pre-Order :", " - ".join(tree.preorder(tree.root)))
print("2. In-Order :", " - ".join(tree.inorder(tree.root)))
print("3. Post-Order :", " - ".join(tree.postorder(tree.root)))

leafs = tree.get_leaf_nodes(tree.root)
print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leafs))

print("======================================")
print("Audit Selesai!")