try:
    x = int(input("Masukan angka : "))
    if x < 10 :
        raise ValueError("Nilai harus lebih dari 10")
except ValueError as err:
    print("ValueError: ", err)
