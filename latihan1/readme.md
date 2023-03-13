class Mobil :
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    
    def into(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")
MobilA = Mobil("Toyota", "Hitam")
MobilA.into() #Output : Mobil Toyota berwarna Hitam
