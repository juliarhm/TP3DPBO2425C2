#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include "Akun.h"
#include "Pembeli.h"
#include "Penjual.h"
#include "Produk.h"
#include "Pesanan.h"
using namespace std;

// === Fungsi Cetak Tabel ===
void printTable(vector<vector<string>> table)
{
    // Hitung lebar kolom
    vector<int> col_widths(table[0].size(), 0);
    for (size_t c = 0; c < table[0].size(); c++)
    {
        int maxw = 0;
        for (size_t r = 0; r < table.size(); r++)
        {
            maxw = max(maxw, (int)table[r][c].size());
        }
        col_widths[c] = maxw;
    }

    // Cetak garis pemisah
    auto print_separator = [&]()
    {
        cout << "+";
        for (size_t c = 0; c < col_widths.size(); c++)
        {
            cout << string(col_widths[c] + 2, '-') << "+";
        }
        cout << "\n";
    };

    // Cetak isi tabel
    print_separator();
    for (size_t r = 0; r < table.size(); r++)
    {
        cout << "|";
        for (size_t c = 0; c < table[r].size(); c++)
        {
            cout << " " << left << setw(col_widths[c]) << table[r][c] << " |";
        }
        cout << "\n";
        if (r == 0)
            print_separator(); // garis setelah header
    }
    print_separator();
}

// === MAIN ===
int main()
{
    // Akun
    Akun akun_pembeli(1, "julia_rahma", "pass123", "juliarahmawati@gmail.com");
    Akun akun_penjual(2, "rahm_0", "111pass", "rahma@gmail.com");
    Akun akun_penjual1(3, "j_polin", "j1245", "jeromepolin@gamil.com");

    // Pengguna
    Pembeli pembeli1("08123456789", "Riau", "Julia", akun_pembeli, "ShopeePay");
    Penjual penjual1("08129876543", "Bandung", "Rahma", akun_penjual,"ElektrikKu", "Menjual barang elektronik", 5);
    Penjual penjual2("08987654300", "Manado", "Jerome", akun_penjual1,"Gramedia", "Menjual buku pelajaran, novel, dan komik", 4.8);

    // Produk
    Produk p1("P001", "Laptop", 7500000, 10, "Laptop Gaming");
    Produk p2("P002", "HP", 3000000, 20, "Smartphone Android");
    Produk p3("P003", "Buku", 95000, 10, "Novel Fiksi");
    Produk p4("P005", "Panci", 30000, 40, "Panci Listrik");
    penjual1.tambahProduk(&p1);
    penjual1.tambahProduk(&p2);
    penjual2.tambahProduk(&p4);

    // Pesanan
    Pesanan pesanan1(p1.get_harga() + p3.get_harga(), "Diproses");
    pesanan1.tambahProduk(&p1);
    pesanan1.tambahProduk(&p3);
    pembeli1.get_RiwayatPesanan().push_back(&pesanan1);

    // === OUTPUT ===
    pembeli1.printPembeli();

    cout << "Riwayat Pesanan\n";
    vector<vector<string>> table = {{"ID", "Nama", "Harga", "Stok", "Kategori"}};
    for (auto pes : pembeli1.get_RiwayatPesanan())
    {
        for (auto prod : pes->get_ListProduk())
        {
            table.push_back({prod->get_id_produk(), prod->get_nama(), to_string(prod->get_harga()), to_string(prod->get_stok()), prod->get_kategori()});
        }
    }
    printTable(table);

    for (auto pes : pembeli1.get_RiwayatPesanan())
    {
        cout << "Total Harga : Rp" << pes->get_totalharga() << endl;
        cout << "Status      : " << pes->get_status() << endl;
    }

    // === DATA PENJUAL ===
    cout << "\n=== DATA PENJUAL ===" << endl;
    penjual1.printPenjual();

    cout << "List Produk\n";
    vector<vector<string>> table2 = {{"ID", "Nama", "Harga", "Stok", "Kategori"}};
    vector<Penjual *> list_penjual = {&penjual1, &penjual2};
    for (auto penjual : list_penjual)
    {
        for (auto prod : penjual->get_ListProduk())
        {
            table2.push_back({prod->get_id_produk(), prod->get_nama(), to_string(prod->get_harga()), to_string(prod->get_stok()), prod->get_kategori()});
        }
    }
    printTable(table2);

    return 0;
}