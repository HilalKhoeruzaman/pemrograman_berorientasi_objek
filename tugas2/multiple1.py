class Santri:
    def __init__(self, nama, no_reg):
        self.nama = nama
        self.no_reg = no_reg
    def ngaji(self):
        print(self.nama, "sedang ngaji")
class Pengabdi:
    def __init__(self, nama, Pengabdian):
        self.nama = nama
        self.Pengabdian = Pengabdian
    def ngabdi(self):
        print(self.nama, "sedang ngabdi")
class SantriPengabdi(Santri, Pengabdi):
    def __init__(self, nama, no_reg, Pengabdian):
        Santri.__init__(self, nama, no_reg)
        Pengabdi.__init__(self, nama, Pengabdian)
    def tadzim(self):
        print(self.nama, "sedang tadzim")

santri_Pengabdi = SantriPengabdi("Hilal Khoeruzaman", "568", "Khodim Kyai")
santri_Pengabdi.ngaji() 
santri_Pengabdi.ngabdi()
santri_Pengabdi.tadzim() 
