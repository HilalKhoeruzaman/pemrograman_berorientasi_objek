
dictionary = {"seribu": 1000, "dua ribu": 2000, "tiga ribu": 3000, "lima ribu": 5000}
try:
    value = dictionary["sepuluh ribu"]
except KeyError:
    print("Key yang anda masukan salah, Coba masukan kembali dengan key yang berbeda! ")