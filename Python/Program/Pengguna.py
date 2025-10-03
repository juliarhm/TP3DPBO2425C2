from Akun import Akun  # import class Akun

class Pengguna:
    def __init__(self, No_Telp, Alamat, Nama, akun: Akun):
        self.__No_Telp = No_Telp
        self.__Alamat = Alamat
        self.__Nama = Nama
        self.__Akun = akun  # composite: Pengguna HAS A Akun

    # Getter & Setter No_Telp
    def getNo_Telp(self):
        return self.__No_Telp

    def setNo_Telp(self, No_Telp):
        self.__No_Telp = No_Telp

    # Getter & Setter Alamat
    def getAlamat(self):
        return self.__Alamat

    def setAlamat(self, Alamat):
        self.__Alamat = Alamat

    # Getter & Setter Nama
    def getNama(self):
        return self.__Nama

    def setNama(self, Nama):
        self.__Nama = Nama

    # Getter & Setter Akun
    def getAkun(self):
        return self.__Akun

    def setAkun(self, akun: Akun):
        self.__Akun = akun

    # Print info pengguna + akun
    def printPengguna(self):
        print(f"Nama              : {self.__Nama}")
        print(f"No. Telp          : {self.__No_Telp}")
        print(f"Alamat            : {self.__Alamat}")
        self.__Akun.printAkun()