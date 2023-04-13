class Hewan:
    def __init__(self, nama, habitat):
        self.nama = nama
        self.habitat = habitat

hewan = Hewan("Andi", 20)
try:
    print(hewan.makanan)
except AttributeError:
    print("Objek tidak ditemukan oleh sistem")