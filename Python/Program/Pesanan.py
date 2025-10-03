from Produk import Produk

class Pesanan:
    def __init__(self, totalharga=0, status="", ListProduk=None):
        self.__totalharga = totalharga
        self.__status = status
        self.__ListProduk = ListProduk if ListProduk is not None else [] # composite: Pesanan HAS-A Produk

    # Getter & Setter total harga
    def get_totalharga(self):
        return self.__totalharga
    def set_totalharga(self, totalharga):
        self.__totalharga = totalharga

    # Getter & Setter status
    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    # Getter & Setter ListProduk
    def get_ListProduk(self):
        return self.__ListProduk
    
    def set_ListProduk(self, ListProduk):
        self.__ListProduk = ListProduk
    
    # Tambah produk ke pesanan
    def tambahProduk(self, produk: Produk):
        self.__ListProduk.append(produk)

    # Method tampilkan pesanan
    def printPesanan(self):
        print("Daftar Produk dalam Pesanan:")
        for produk in self.__ListProduk:
            produk.printProduk()
        print(f"Total Harga : Rp{self.__totalharga}")
        print(f"Status      : {self.__status}")