class Penulis :
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul
        self.Informasi = Informasi ()

    def __repr__(self):
        return f'{self.nama}'
        return f'{self.judul}'
class Informasi :
    def __init__(self):
        self.info = []
    def add_informasi(self, penerbit, harga):
        self.info.append(penerbit)
        self.info.append(harga)
    def del_informasi(self, penerbit, harga):
        self.info.append(penerbit)
        self.info.append(harga)
class Buku :
    def __init__(self, penulis):
        self.penulis = penulis
    def __repr__(self):
        return f'{self.penulis}'

penulis = Penulis("Dee Lestari", "Aroma Karsa")
info = Informasi()
penulis.Informasi.add_informasi(2011, "Rp. 110.000")
print(repr(penulis))
print(penulis.Informasi.info)
    
