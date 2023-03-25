class Film:
    def __init__(self, nama, durasi):
        self.nama = nama
        self.durasi = durasi
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Durasi: {self.durasi}")
class Aksi:
    def __init__(self, negara, aktor):
        self.negara = negara
        self.aktor = aktor
    def display_info(self):
        print(f"negara: {self.negara}")
        print(f"aktor: {self.aktor}")
class Komedi:
    def __init__(self, produser, aktor):
        self.produser = produser
        self.aktor = aktor
    def display_info(self):
        print(f"produser: {self.produser}")
        print(f"aktor: {self.aktor}")
class Drunken_Master(Aksi, Komedi):
    def __init__(self, nama, durasi, negara, aktor, produser):
        Film.__init__(self, nama, durasi)
        Aksi.__init__(self, negara, aktor)
        Komedi.__init__(self, produser, aktor)
    def display_info(self):
        super().display_info()  
        print(f"Nama: {self.nama}")
        print(f"Durasi: {self.durasi}")
        print(f"Negara: {self.negara}")
        print(f"Aktor: {self.aktor}")
        print(f"Produser: {self.produser}")

# contoh penggunaan
drunkenMasterA = Drunken_Master("Drunken Master", "3 Jam", "Aksi-Komedi", "Jackie Chan", "Ng See-yuen")
drunkenMasterA.display_info()