produk = {"Laptop": 5500000, "Smartphone": 3000000, "Tablet": 2000000, "Smartwatch":
1500000, "Headphone": 500000}

while True:
    nama = input("masukkan nama : ")
    umur = int(input("umur  : "))
    if umur > 17:
        print("")
    else:
        print("maaf umur anda masih kurang ")
    break

member = input("apakah anda memiliki member : ")
if member == "ya":
    penawaran = int(input("ajukan penawaran anda: "))
    if penawaran > 50000:
        print("maaf penawaran ditolak")
    elif penawaran < 3000:
        print("penawaran berhasil")
else:
    print("lanjutkan transakasi")

gadget = input("masukkan produk yang ingin dibeli : ")
if gadget == produk:
    print("lanjutkan transakasi")
else: 
    print()

    
unit = int (input("masukkan berapa unit produk yang ingin dibeli : "))
print(unit)
tawar = input("apakah anda ingin melakukan penawaran  : ")

print(nama)
print(umur)
print(member)
print(gadget)
print(unit)



