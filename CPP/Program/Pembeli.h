#ifndef PEMBELI_H
#define PEMBELI_H
#include <iostream>
#include <string>
#include <vector>
#include "Pengguna.h"
#include "Pesanan.h"
using namespace std;

class Pembeli : public Pengguna
{
private:
    string MetodePembayaran;
    vector<Pesanan *> RiwayatPesanan;

public:
    Pembeli(string t = "", string a = "", string n = "", Akun ak = Akun(), string mp = "")
        : Pengguna(t, a, n, ak), MetodePembayaran(mp) {}

    string get_MetodePembayaran() { return MetodePembayaran; }
    void set_MetodePembayaran(string m) { MetodePembayaran = m; }

    vector<Pesanan *> &get_RiwayatPesanan() { return RiwayatPesanan; }

    void printPembeli()
    {
        printPengguna();
        cout << "Metode Pembayaran : " << MetodePembayaran << endl;
    }
};
#endif
