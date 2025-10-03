class Produk:
    def __init__(self, id_produk="", nama="", harga=0, stok=0, kategori=""):
        self.__id_produk = id_produk
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok
        self.__kategori = kategori

    # Getter & Setter id_produk
    def get_id_produk(self):
        return self.__id_produk
    def set_id_produk(self, id_produk):
        self.__id_produk = id_produk

    # Getter & Setter nama
    def get_nama(self):
        return self.__nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter & Setter harga
    def get_harga(self):
        return self.__harga
    def set_harga(self, harga):
        self.__harga = harga

    # Getter & Setter stok
    def get_stok(self):
        return self.__stok
    def set_stok(self, stok):
        self.__stok = stok

    # Getter & Setter kategori
    def get_kategori(self):
        return self.__kategori
    def set_kategori(self, kategori):
        self.__kategori = kategori

    # Method tampilkan produk
    def printProduk(self):
        print(f"{self.__id_produk} - Rp{self.__harga} | Stok: {self.__stok} | Kategori: {self.__kategori}")