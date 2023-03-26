class Santri:
    def __init__(self, name, no_reg, kamar):
        self.name = name
        self.no_reg = no_reg
        self.kamar = kamar
    def get_name(self):
        return self.name
    def get_no_reg(self):
        return self.no_reg
    def get_kamar(self):
        return self.kamar
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Nomor Registrasi : {self.no_reg}")
        print(f"kamar : {self.kamar}")
class Formal(Santri):
    def __init__(self, name, no_reg, kamar, sekolah):
        super().__init__(name, no_reg, kamar)
        self.sekolah = sekolah
    def get_sekolah(self):
        return self.sekolah
class Takhassus(Santri):
    def __init__(self, name, no_reg, kamar, madrasah):
        super().__init__(name, no_reg, kamar)
        self.madrasah = madrasah
    def get_madrasah(self):
        return self.madrasah
# Hierarchical Inheritance
class JuniorTakhassus(Takhassus):
    def __init__(self, name, no_reg, kamar, madrasah, kelas):
        super().__init__(name, no_reg, kamar, madrasah)
        self.kelas = kelas
    def get_kelas(self):
        return self.kelas
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.name}")
        print(f"Nomor Registrasi: {self.no_reg}")
        print(f"Kamar: {self.kamar}")
        print(f"Madrasah: {self.madrasah}")
        print(f"Kelas: {self.kelas}")

juniorTakhassusA = JuniorTakhassus("Muhammad Ridwan", 335, 12, "Madrasah Tahsinul Akhlaq ", 5)
juniorTakhassusA.display_info()