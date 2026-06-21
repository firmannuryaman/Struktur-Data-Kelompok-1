class Node:
    def __init__(self, nama):
        self.nama = nama
        self.children = []

    def tambah_anak(self, node):
        self.children.append(node)

def tampilkan_tree(node, level=0):
    print("  " * level + "- " + node.nama)

    for child in node.children:
        tampilkan_tree(child, level + 1)

# Membuat tree distribusi
gudang = Node("Gudang Pusat")

jakarta = Node("Cabang Jakarta")
bandung = Node("Cabang Bandung")

pelA = Node("Pelanggan A")
pelB = Node("Pelanggan B")
pelC = Node("Pelanggan C")
pelD = Node("Pelanggan D")

gudang.tambah_anak(jakarta)
gudang.tambah_anak(bandung)

jakarta.tambah_anak(pelA)
jakarta.tambah_anak(pelB)

bandung.tambah_anak(pelC)
bandung.tambah_anak(pelD)

tampilkan_tree(gudang)