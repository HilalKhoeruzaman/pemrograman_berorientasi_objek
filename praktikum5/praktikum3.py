try:
    with open("LaporanKeuangan.txt") as file:
         data = file.read()
except FileNotFoundError:
    print("Mohon maaf file yang anda cari tidak ditemukan!")