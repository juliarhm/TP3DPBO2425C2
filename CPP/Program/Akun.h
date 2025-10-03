#ifndef AKUN_H
#define AKUN_H
#include <iostream>
#include <string>
using namespace std;

class Akun
{
private:
    int IdAkun;
    string Username, Password, Email;

public:
    Akun(int id = 0, string user = "", string pass = "", string email = "")
    {
        IdAkun = id;
        Username = user;
        Password = pass;
        Email = email;
    }
    int getIdAkun() { return IdAkun; }
    void setIdAkun(int id) { IdAkun = id; }
    string getUsername() { return Username; }
    void setUsername(string u) { Username = u; }
    string getPassword() { return Password; }
    void setPassword(string p) { Password = p; }
    string getEmail() { return Email; }
    void setEmail(string e) { Email = e; }

    void printAkun()
    {
        cout << "ID Akun           : " << IdAkun << endl;
        cout << "Username          : " << Username << endl;
        cout << "Password          : " << Password << endl;
        cout << "Email             : " << Email << endl;
    }
};
#endif