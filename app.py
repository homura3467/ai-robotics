# Program Mengira Jumlah Pembelian

jumlah_keseluruhan = 0.0

print("=== SISTEM KIRAAN PEMBELIAN ===")
bilangan_barang = int(input("Masukkan bilangan jenis barang yang dibeli: "))

for i in range(bilangan_barang):
    print(f"\nBarang ke-{i + 1}:")
    nama_barang = input("Nama barang: ")
    harga = float(input("Harga seunit (RM): "))
    kuantiti = int(input("Kuantiti: "))
    
    jumlah_barang = harga * kuantiti
    jumlah_keseluruhan += jumlah_barang
    print(f"Subtotal untuk {nama_barang}: RM {jumlah_barang:.2f}")

print("\n===============================")
print(f"JUMLAH PERLU DIBAYAR: RM {jumlah_keseluruhan:.2f}")
print("===============================")
