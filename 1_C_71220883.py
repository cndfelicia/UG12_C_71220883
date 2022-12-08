def balikhuruf(a):
    akhir=' '
    for i in a:
        akhir=i+akhir
    return akhir
a=input("Masukkan Kata atau angka : ")
print(balikhuruf(a))
