#ifndef PRODUK_H
#define PRODUK_H
#include <iostream>
#include <string>
using namespace std;

class Produk
{
private:
    string id_produk, nama, kategori;
    int harga, stok;

public:
    Produk(string id = "", string n = "", int h = 0, int s = 0, string k = "")
    {
        id_produk = id;
        nama = n;
        harga = h;
        stok = s;
        kategori = k;
    }
    string get_id_produk() { return id_produk; }
    void set_id_produk(string id) { id_produk = id; }
    string get_nama() { return nama; }
    void set_nama(string n) { nama = n; }
    int get_harga() { return harga; }
    void set_harga(int h) { harga = h; }
    int get_stok() { return stok; }
    void set_stok(int s) { stok = s; }
    string get_kategori() { return kategori; }
    void set_kategori(string k) { kategori = k; }

    void printProduk()
    {
        cout << id_produk << " - " << nama << " Rp" << harga << " | Stok: " << stok << " | Kategori: " << kategori << endl;
    }
};
#endif
