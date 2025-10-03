#ifndef PENJUAL_H
#define PENJUAL_H
#include <iostream>
#include <string>
#include <vector>
#include "Pengguna.h"
#include "Produk.h"
using namespace std;

class Penjual : public Pengguna
{
private:
    string NamaToko, Deskripsi;
    double RatingToko;
    vector<Produk *> ListProduk;

public:
    Penjual(string t = "", string a = "", string n = "", Akun ak = Akun(),
            string toko = "", string desk = "", double rating = 0.0)
        : Pengguna(t, a, n, ak), NamaToko(toko), Deskripsi(desk), RatingToko(rating) {}

    string get_NamaToko() { return NamaToko; }
    void set_NamaToko(string t) { NamaToko = t; }
    string get_Deskripsi() { return Deskripsi; }
    void set_Deskripsi(string d) { Deskripsi = d; }
    double get_RatingToko() { return RatingToko; }
    void set_RatingToko(double r) { RatingToko = r; }

    vector<Produk *> &get_ListProduk() { return ListProduk; }
    void tambahProduk(Produk *p) { ListProduk.push_back(p); }

    void printPenjual()
    {
        printPengguna();
        cout << "Nama Toko         : " << NamaToko << endl;
        cout << "Deskripsi         : " << Deskripsi << endl;
        cout << "Rating Toko       : " << RatingToko << endl;
    }
};
#endif
