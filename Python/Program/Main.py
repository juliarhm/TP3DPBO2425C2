from Akun import Akun
from Pengguna import Pengguna
from Pembeli import Pembeli
from Penjual import Penjual
from Produk import Produk
from Pesanan import Pesanan

if __name__ == "__main__":
    # === Buat Akun ===
    akun_pembeli = Akun(1, "julia_rahma", "pass123", "juliarahmawati@gmail.com")
    akun_penjual = Akun(2, "rahm_0", "111pass", "rahma@gmail.com")
    akun_penjual1 = Akun(3, "j_polin", "j1245", "jeromepolin@gamil.com")

    # === Buat Pengguna ===
    pembeli1 = Pembeli("08123456789", "Riau", "Julia", akun_pembeli, "ShopeePay", [])
    penjual1 = Penjual("08129876543", "Bandung", "Rahma", akun_penjual, "ElektrikKu", "Menjual barang elektronik", 5)
    penjual2 = Penjual("08987654300", "Manado", "Jerome", akun_penjual1, "Gramedia", "Menjual buku pelajaran, novel, dan komik", 4.8)

    # === Buat Produk ===
    produk1 = Produk("P001","Laptop", 7500000, 10, "Laptop Gaming")
    produk2 = Produk("P002", "HP", 3000000, 20, "Smartphone Android")
    produk3 = Produk("P003", "Buku", 95000, 10, "Novel Fiksi")
    produk4 = Produk("P004", "Baju", 85000, 20, "Gamis tunik")
    produk5 = Produk("P005", "Panci", 30000, 40, "Panci Listrik")

    # Tambahkan produk ke toko penjual
    penjual1.get_ListProduk().append(produk1)
    penjual1.get_ListProduk().append(produk2)
    penjual2.get_ListProduk().append(produk3)

    # === Buat Pesanan oleh pembeli ===
    list_produk_pesanan = [produk1, produk3, produk5]
    total_harga = sum([p.get_harga() for p in list_produk_pesanan])
    pesanan1 = Pesanan(total_harga, "Diproses", list_produk_pesanan)

    # Tambahkan riwayat pesanan ke pembeli
    pembeli1.get_RiwayatPesanan().append(pesanan1)

    # === OUTPUT DEMO ===
    pembeli1.printPembeli()
    # header tabel
    print("Riwayat Pesanan ")
    table = [
        ["ID", "Nama", "Harga", "Stok", "Kategori"]
    ]

    # loop semua pesanan pembeli
    for pesanan in pembeli1.get_RiwayatPesanan():
        for produk in pesanan.get_ListProduk():
            row = [
                produk.get_id_produk(),
                produk.get_nama(),
                str(produk.get_harga()),
                str(produk.get_stok()),
                produk.get_kategori()
            ]
            table.append(row)

    # hitung lebar kolom
    col_widths = [max(len(str(row[c])) for row in table) for c in range(len(table[0]))]

    # fungsi cetak garis
    def print_separator():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    # cetak tabel
    print_separator()
    for r, row in enumerate(table):
        print("|" + "|".join(f" {str(row[c]).ljust(col_widths[c])} " for c in range(len(row))) + "|")
        if r == 0:  # garis setelah header
            print_separator()
    print_separator()

    # total harga & status
    for i, pesanan in enumerate(pembeli1.get_RiwayatPesanan(), start=1):
        print(f"Total Harga : Rp{pesanan.get_totalharga()}")
        print(f"Status      : {pesanan.get_status()}")

    # 

    print("\n=== DATA PENJUAL ===")
    penjual1.printPenjual()
    print("List Produk ")
    # 1. Header tabel
    table = [
        ["ID", "Nama", "Harga", "Stok", "Kategori"]
    ]

    # 2. Tambahkan data produk ke tabel
    list_penjual = [penjual1, penjual2]

    for penjual in list_penjual:
        for p in penjual.get_ListProduk():
            row = [
                p.get_id_produk(),
                p.get_nama(),
                str(p.get_harga()),
                str(p.get_stok()),
                p.get_kategori()
            ]
            table.append(row)

    # 3. Hitung lebar kolom (setelah semua data masuk)
    col_widths = [max(len(str(row[c])) for row in table) for c in range(len(table[0]))]

    # 4. Fungsi cetak garis
    def print_separator():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    # 5. Cetak tabel
    print_separator()
    for r, row in enumerate(table):
        print("|" + "|".join(f" {str(row[c]).ljust(col_widths[c])} " for c in range(len(row))) + "|")
        if r == 0:  # garis setelah header
            print_separator()
    print_separator()