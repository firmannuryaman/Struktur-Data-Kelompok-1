from collections import deque

antrian_pengiriman = deque()

# Barang masuk ke gudang
antrian_pengiriman.append("Paket A")
antrian_pengiriman.append("Paket B")
antrian_pengiriman.append("Paket C")

print("Antrian Pengiriman:")
print(antrian_pengiriman)

# Barang dikirim sesuai urutan masuk
while antrian_pengiriman:
    paket = antrian_pengiriman.popleft()
    print(f"Mengirim {paket}")