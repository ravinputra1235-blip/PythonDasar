baris = int(input("Masukkan jumlah baris: "))

print("Segitiga Bintang Siku Siku")

for i in range(1, baris + 1):
    for j in range(i):
        print("*", end=" ")
    print()

    baris = int(input("Masukkan jumlah baris: "))

for i in range(baris, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()