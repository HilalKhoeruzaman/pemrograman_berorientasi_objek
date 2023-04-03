class Mobil :
    def kecepatan(self):
        print("Mobil memiliki kecepatan")
class Toyota(Mobil):
    def kecepatan(self):
        print("Mobil Toyota memiliki kecepatan 140km/jam")
class Alphard(Mobil):
    def kecepatan(self):
        print("Mobil Alphard memiliki kecepatan 150km/jam")

def fast(mobil):
    mobil.kecepatan()

mobil = Mobil()
toyota = Toyota()
alphard = Alphard()

fast(mobil)
fast(toyota)
fast(alphard)
