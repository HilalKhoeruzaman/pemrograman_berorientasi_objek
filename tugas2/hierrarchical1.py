class Makhluk_Hidup:
    def __init__(self, nama, habitat):
        self.nama = nama
        self.habitat = habitat
    def get_nama(self):
        return self.nama
    def get_habitat(self):
        return self.habitat
    def display_info(self):
        print(f"nama : {self.nama}")
        print(f"habitat : {self.habitat}")
class Karnivora(Makhluk_Hidup):
    def __init__(self, nama, habitat, daging):
        super().__init__(nama, habitat)
        self.daging = daging
    def get_daging(self):
        return self.daging
class Herbivora(Makhluk_Hidup):
    def __init__(self, nama, habitat, tumbuhan):
        super().__init__(nama, habitat)
        self.tumbuhan = tumbuhan
    def get_tumbuhan(self):
        return self.tumbuhan
class Omnivora (Makhluk_Hidup):
    def __init__(self, nama, habitat, daging_tumbuhan):
        super().__init__(nama, habitat)
        self.daging_tumbuhan = daging_tumbuhan
    def get_daing_tumbuhan(self):
        return self.daging_tumbuhan
# Hierarchical Inheritance
class Ular(Karnivora):
    def __init__(self, nama, habitat, daging, panjang):
        super().__init__(nama, habitat, daging)
        self.panjang = panjang
    def get_panjang(self):
        return self.panjang
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Habitat: {self.habitat}")
        print(f"Daging: {self.daging}")
        print(f"panjang: {self.panjang}")
       
UlarA = Ular ("Python", "Hutan Sumatra", "Rusa", "3 meter")
UlarA.display_info()