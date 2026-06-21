stack_barang = []

# Barang dimasukkan ke kontainer
stack_barang.append("Box A")
stack_barang.append("Box B")
stack_barang.append("Box C")

print("Isi Kontainer:")
print(stack_barang)

# Bongkar barang
while stack_barang:
    barang = stack_barang.pop()
    print(f"Membongkar {barang}")