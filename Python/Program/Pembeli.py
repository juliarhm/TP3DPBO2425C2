from Pengguna import Pengguna

class Pembeli(Pengguna):
    def __init__(self, No_Telp="", Alamat="", Nama="", akun=None, MetodePembayaran="", RiwayatPesanan=""):
        # panggil constructor Pengguna
        super().__init__(No_Telp, Alamat, Nama, akun)
        self.__MetodePembayaran = MetodePembayaran
        self.__RiwayatPesanan = RiwayatPesanan if RiwayatPesanan is not None else []

    # Getter & Setter metode pembayaran
    def get_MetodePembayaran(self):
        return self.__MetodePembayaran
    
    def set_MetodePembayaran(self, MetodePembayaran):
        self.__MetodePembayaran = MetodePembayaran

    # Getter & Setter RiwayatPesanan
    def get_RiwayatPesanan(self):
        return self.__RiwayatPesanan
    
    def set_RiwayatPesanan(self, RiwayatPesanan):
        self.__RiwayatPesanan = RiwayatPesanan

    # Method Tampilkan 
    def printPembeli(self):
        self.printPengguna()  # tampilkan data dari class Pengguna
        print("Metode Pembayaran : ", self.get_MetodePembayaran())
