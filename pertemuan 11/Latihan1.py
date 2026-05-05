class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 1. INSERT
    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)

        if self.root is None:
            self.root = new
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return

        P = None
        Q = self.root

        while Q is not None:
            P = Q
            if id_buku < Q.id:
                Q = Q.left
            elif id_buku > Q.id:
                Q = Q.right
            else:
                print("[INSERT] ID sudah ada!")
                return

        if id_buku < P.id:
            P.left = new
        else:
            P.right = new

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    # 2. SEARCH
    def search(self, id_buku):
        Q = self.root
        while Q is not None:
            if id_buku == Q.id:
                return Q
            elif id_buku < Q.id:
                Q = Q.left
            else:
                Q = Q.right
        return None

    # 3. INORDER
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    # 4. MIN
    def get_min(self):
        Q = self.root
        while Q.left is not None:
            Q = Q.left
        return Q

    # 4. MAX
    def get_max(self):
        Q = self.root
        while Q.right is not None:
            Q = Q.right
        return Q

    # 5. HEIGHT
    def height(self, node):
        if node is None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return max(left_h, right_h) + 1




print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

bst = BST()

# Input data
bst.insert(50, "Hujan")
bst.insert(30, "Pulang")
bst.insert(70, "Laut Bercerita")
bst.insert(20, "Serial Anak Mamak")
bst.insert(40, "Ayahku Bukan Pembohong")
bst.insert(60, "Filosofi Teras")
bst.insert(80, "Pergi")

# Inorder traversal
print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.inorder(bst.root)

# Search
print("\n[SEARCH] Mencari ID 60...", end=" ")
hasil = bst.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end=" ")
hasil = bst.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

# Statistik
min_node = bst.get_min()
max_node = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_node.id}")
print(f"[STATISTIK] ID Terbesar: {max_node.id}")

# Height
print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")

print("=========================================")
print("Simulasi Selesai!")