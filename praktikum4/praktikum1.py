class Peneliti :
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul
class Jurnal :
    def __init__(self, peneliti, judul):
        self.peneliti = peneliti
        self.judul = judul
    def judul_jurnal(self) :
        for peneliti in self.peneliti :
            print(peneliti.peneliti, peneliti.judul)

jurnal1 = Jurnal("Dampak Game Mobile Legend pada Moral Anak Bangsa", "Hilal Khoeruzaman")
jurnal2 = Jurnal("Agama dan Teknologi", "Reza Rahardian")
jurnal = Jurnal([jurnal1, jurnal2], "Rangkuman Jurnal")
jurnal.judul_jurnal()