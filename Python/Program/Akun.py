class Akun:
    def __init__(self, IdAkun="", Username="", Password="", Email=""):
        self.__IdAkun = IdAkun
        self.__Username = Username
        self.__Password = Password
        self.__Email = Email

    # Getter & Setter IdAkun
    def getIdAkun(self):
        return self.__IdAkun

    def setIdAkun(self, IdAkun):
        self.__IdAkun = IdAkun

    # Getter & Setter Username
    def getUsername(self):
        return self.__Username

    def setUsername(self, Username):
        self.__Username = Username

    # Getter & Setter Password
    def getPassword(self):
        return self.__Password

    def setPassword(self, Password):
        self.__Password = Password

    # Getter & Setter Email
    def getEmail(self):
        return self.__Email

    def setEmail(self, Email):
        self.__Email = Email

    # Method untuk menampilkan data
    def printAkun(self):
        print("ID Akun           :", self.getIdAkun())
        print("Username          :", self.getUsername())
        print("Password          :", self.getPassword())
        print("Email             :", self.getEmail())