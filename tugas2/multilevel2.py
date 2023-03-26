class Ikan:
    def __init__(self, name):
        self.name = name
    def Rasa(self):
        print("Ikan hidup di air")
class Lele(Ikan):
    def __init__(self, name, ukuran):
        super().__init__(name)
        self.ukuran = ukuran
    def Kumis(self):
        print("Ikan memiliki kumis")
class LeleJumbo(Lele):
    def __init__(self, name, ukuran, asal):
        super().__init__(name, ukuran)
        self.asal = asal
    def Kumis(self):
        print("Ikan lele Jumbo memiliki ukuran yang lebih besar dibandingkan yang lain")

leleJumboA = LeleJumbo("Clarias gariepinus", "80 cm", "Afrika")
leleJumboA.Kumis()