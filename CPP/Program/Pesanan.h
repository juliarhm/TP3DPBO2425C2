#ifndef PESANAN_H
#define PESANAN_H
#include <iostream>
#include <string>
#include <vector>
#include "Produk.h"
using namespace std;

class Pesanan
{
private:
    int totalharga;
    string status;
    vector<Produk *> ListProduk;

public:
    Pesanan(int t = 0, string s = "") : totalharga(t), status(s) {}

    int get_totalharga() { return totalharga; }
    void set_totalharga(int t) { totalharga = t; }
    string get_status() { return status; }
    void set_status(string s) { status = s; }

    vector<Produk *> &get_ListProduk() { return ListProduk; }
    void tambahProduk(Produk *p) { ListProduk.push_back(p); }

    void printPesanan()
    {
        cout << "Daftar Produk dalam Pesanan:" << endl;
        for (auto p : ListProduk)
            p->printProduk();
        cout << "Total Harga : Rp" << totalharga << endl;
        cout << "Status      : " << status << endl;
    }
};
#endif
