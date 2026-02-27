baris = int(input("Masukkan jumlah baris: "))

for i in range(1, baris + 1):
    # spasi
    for j in range(baris - i):
        print(" ", end="")
    # bintang
    for k in range(i):
        print("* ", end="")
    print()