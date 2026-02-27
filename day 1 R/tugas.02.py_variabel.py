import math

jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

volume = math.pi * jari**2 * tinggi

print("Volume tabung =", volume)

panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

volume = panjang * lebar * tinggi

print("Volume balok =", volume)