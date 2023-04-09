class Mahasiswa :
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def __repr__(self):
        return f'{self.nama}{self.nim}'
class Anggota :
    def __init__(self):
        self.anggota = []
    def add_anggota(self, anggota):
        self.anggota.append(anggota)
class kel_KKN :
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa

mahasiswa1 = Mahasiswa("Hilal Khoeruzaman", "210511007")
mahasiswa2 = Mahasiswa("Hilal Khoerul Anwar", "210511008")
mahasiswa = Anggota()
mahasiswa.add_anggota(mahasiswa1)
mahasiswa.add_anggota(mahasiswa2)
kelompok = kel_KKN(mahasiswa)
print(repr(kelompok.mahasiswa.anggota))