class Santri :
    def __init__(self, nama):
        self.nama = nama
class Kyai :
    def __init__(self, nama):
        self.nama = nama
class Pesantren :
    def __init__ (self, santri, kyai):
        self.santri = santri 
        self.kyai = kyai

santriA = Santri("Abdul Somad")
kyaiA = Kyai("Kyai Abdul Muhib")
pesantrenA = Pesantren(santriA, kyaiA)
print(pesantrenA.santri.nama)
print(kyaiA.nama)

