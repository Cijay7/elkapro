# if
# nilai = 60
# if nilai >= 75:
#     print("Lulus")
# else:
#     print("Tidak Lulus")    
# # if...else
# nilai = float(input("Masukkan nilai Anda: "))
# if nilai >= 75:
#     print("Lulus")
# else:
#     print("Tidak Lulus")


# # if...elif...else
# nilai = int(input("Masukkan nilai Anda: "))
# if nilai >= 90:
#     print("Predikat A")
# elif nilai >= 75:
#     print("Predikat B")
# elif nilai >= 60:
#     print("Predikat C")
# else:
#     print("Predikat D")


# # switch case
# menu = int(input("Pilih menu (1-3): "))
# match menu:
#     case 1:
#         print("Nasi Goreng")
#     case 2:
#         print("Mie Ayam")
#     case 3:
#         print("Bakso")
    # case _:
    #     print("Menu tidak tersedia")


angka = int(input("Masukkan angka "))
angka2 = int(input("Masukkan angka kedua "))
angka3 = int(input("Masukkan angka ketiga "))

if angka > angka2 or angka > angka3:
    print(f"Angka terbesar adalah {angka3}")
    