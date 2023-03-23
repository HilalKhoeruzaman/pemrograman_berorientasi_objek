class Bangunan:
    def __init__(self, lantai , warna):
        self.lantai = lantai
        self.warna = warna
    def berteduh(self):
        print("Bangunan ini berfungsi untuk berteduh")
class Hotel(Bangunan):
    def __init__(self, lantai, warna, acara):
        super().__init__(lantai, warna)
        self.acara = acara
    def pesta(self):
        print("Hotel ini bisa dipakai untuk acara resepsi pernikahan")

hotelB = Hotel( 20 , "Merah", "Resepsi Pernikahan" )
hotelB.berteduh()
hotelB.pesta()
