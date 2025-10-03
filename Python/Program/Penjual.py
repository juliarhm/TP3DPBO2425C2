from Pengguna import Pengguna

class Penjual(Pengguna):
    def __init__(self, No_Telp="", Alamat="", Nama="", akun=None, NamaToko="", Deskripsi="", RatingToko="", ListProduk=None):
        # panggil constructor Pengguna
        super().__init__(No_Telp, Alamat, Nama, akun)
        self.__NamaToko = NamaToko
        self.__Deskripsi = Deskripsi
        self.__RatingToko = RatingToko
        self.__ListProduk = ListProduk if ListProduk is not None else [] # composite Penjual Has A Produk

    # Getter & Setter NamaToko
    def get_NamaToko(self):
        return self.__NamaToko
    
    def set_NamaToko(self, NamaToko):
        self.__NamaToko = NamaToko

    # Getter & Setter Deskripsi
    def get_Deskripsi(self):
        return self.__Deskripsi
    
    def set_Deskripsi(self, Deskripsi):
        self.__Deskripsi = Deskripsi

    # Getter & Setter RatingToko
    def get_RatingToko(self):
        return self.__RatingToko
    
    def set_RatingToko(self, RatingToko):
        self.__RatingToko = RatingToko

    # Getter & Setter ListProduk
    def get_ListProduk(self):
        return self.__ListProduk
    
    def set_ListProduk(self, ListProduk):
        self.__ListProduk = ListProduk
    
    def tambahProduk(self, produk):
        self.__ListProduk.append(produk)

    # Method Tampilkan
    def printPenjual(self):
        self.printPengguna()  # data umum dari Pengguna
        print("Nama Toko         :", self.get_NamaToko())
        print("Deskripsi         :", self.get_Deskripsi())
        print("Rating Toko       :", self.get_RatingToko())
