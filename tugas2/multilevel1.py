class Buah:
    def __init__(self, name):
        self.name = name
    def Rasa(self):
        print("Buah-buahan memiliki rasa")
class Pisang(Buah):
    def __init__(self, name, ukuran):
        super().__init__(name)
        self.ukuran = ukuran
    def Rasa(self):
        print("Pisang memiliki rasa yang manis")
class PisangAmbon(Pisang):
    def __init__(self, name, ukuran, asal):
        super().__init__(name, ukuran)
        self.asal = asal
    def Rasa(self):
        print("Pisang ambon memiliki rasa yang manis")

pisangAmbonA = PisangAmbon("Pisang Ambon"," Kecil", "Ambon")
pisangB = Pisang("Pisang Raja", "Gede")
buahC = Buah("Buah apa yang enak?")
pisangAmbonA.Rasa()
pisangB.Rasa()
buahC.Rasa()