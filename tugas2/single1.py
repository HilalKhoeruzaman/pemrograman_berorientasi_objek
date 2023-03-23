class Ular:
    def __init__(self, nama, panjang):
        self.nama = nama
        self.panjang = panjang
    def melata(self):
        print(f"{self.nama} sedang melata.")
class Cobra(Ular):
    def __init__(self, nama, panjang, bisa):
        super().__init__(nama, panjang)
        self.bisa = bisa
    def mematuk(self):
        print(f"{self.nama} itu {self.bisa} sampai membuat orang mati.")

cobraA = Cobra("King Cobra", 2, "mematikan")
cobraA.melata() 
cobraA.mematuk() 