print("Nama : Hilal Khoeruzaman\nNIM : 210511007\nKelas : R1 (TI21A)\n")
class fahrenheit:
    @staticmethod
    def celcius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
mycelcius = 75
myfahrenheit = fahrenheit.celcius_to_fahrenheit(mycelcius)

print("konversi",mycelcius, "derajat celcius adalah",myfahrenheit, "derajat fahrenheit")
class kelvin:
    @staticmethod
    def celcius_to_kelvin(celsius):
        return celsius + 273
mycelcius = 80
mykelvin = kelvin.celcius_to_kelvin(mycelcius)
print("konversi",mycelcius, "derajat celcius adalah",mykelvin, "derajat kelvin")

class reamur:
    @staticmethod
    def celcius_to_reamur(celsius):
        return celsius * 4/5

mycelcius = 70
myreamur = reamur.celcius_to_reamur(mycelcius)
print("konversi",mycelcius, "derajat celcius adalah",myreamur, "derajat reamur")