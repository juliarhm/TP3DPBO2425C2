#ifndef PENGGUNA_H
#define PENGGUNA_H
#include <iostream>
#include <string>
#include "Akun.h"
using namespace std;

class Pengguna
{
protected:
    string No_Telp, Alamat, Nama;
    Akun akun;

public:
    Pengguna(string t = "", string a = "", string n = "", Akun ak = Akun())
        : No_Telp(t), Alamat(a), Nama(n), akun(ak) {}

    string getNo_Telp() { return No_Telp; }
    void setNo_Telp(string t) { No_Telp = t; }
    string getAlamat() { return Alamat; }
    void setAlamat(string a) { Alamat = a; }
    string getNama() { return Nama; }
    void setNama(string n) { Nama = n; }
    Akun getAkun() { return akun; }
    void setAkun(Akun ak) { akun = ak; }

    void printPengguna()
    {
        cout << "Nama              : " << Nama << endl;
        cout << "No. Telp          : " << No_Telp << endl;
        cout << "Alamat            : " << Alamat << endl;
        akun.printAkun();
    }
};
#endif