awal=input("Masukkan angka : ")
tengah=input("Masukkan angka yg dihitung : ")

a=0
for b in list (awal):
    if b == tengah:
        a=a+1
print("Angka",tengah,"muncul sebanyak",a,"kali")
