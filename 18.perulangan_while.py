# PERULANGAN WHILE
print("===============PERULANGAN WHILE===============")
# Struktur perulangan (atau dalam bahasa inggris disebut dengan loop) adalah instruksi kode program yang bertujuan untuk mengulang beberapa baris perintah
# Dalam merancang perulangan, kita setidaknya harus mengetahui 3 komponen: kondisi awal perulangan, kondisi pada saat perulangan, dan kondisi yang harus dipenuhi agar perulangan berhenti

# format dasar struktur perulangan while:
# start;
# while argument:
#       statement
#       statement
#       dan seterusnya
#       increment

# start : merupakan perintah inisialisasi variabel counter
# argument : memiliki kondisi yang harus dipenuhi agar perulangan berjalan
# increment : untuk menaikan dan menurunkan angka counter perulangan (i += 1 atau i -= 1)

# dalam hal ini, selama argument terpenuhi (True) maka statement akan selalu dijalankan ketika tidak ada increment

# PERULANGAN WHILE INCREMENT NAIK
print("===============PERULANGAN WHILE INCREMENT NAIK===============")

i = 1  # variabel counter ini akan dipakai untuk menentukan jumlah perulangan naik
while i < 5:  # ini kondisi, artinya selama i < 5 maka perulangan akan berjalan
    print("Hello World1", i)  # ini perintah yang keluar dalam output
    i += 1  # increment naik 1 setiap dalam perulangan

# CATATAN : ketika dalam suatu perulangan while tidak dikasih increment, maka perulangannya akan terus dijalankan sampai tak hingga (dikenal dengan infinity loop)

# PERULANGAN WHILE INCREMENT TURUN
print("===============PERULANGAN WHILE INCREMENT TURUN===============")

i = 10  # variabel counter ini akan dipakai untuk menentukan jumlah perulangan turun
while i >= 1:  # ini kondisi, artinya selama i >= 1 maka perulangan akan berjalan
    print("Hello World1", i)  # ini perintah yang keluar dalam output
    i -= 1  # increment turun 1 setiap dalam perulangan

# Perulangan While untuk deret kelipatan 3 dari 3 sampai 99
i = 3
while i < 100:
    print(i)
    i = i + 3
    i += 0

# PERULANGAN WHILE Dengan Tipe Boolean
print("===============WHILE Dengan Tipe Boolean===============")
start = True
angka = 0

while start:
    print("masih didalam while", angka)
    if angka is 10:
        start = False
        print("Stop di 10")
    angka += 1

# KOMBINASI WHILE dengan ELSE, BREAK, CONTINUE, PASS
print("===============WHILE Dengan ELSE===============")
angka = 0
while angka < 10:
    print("nilai angka adalah : ", angka)
    angka += 1
else:
    print("nilai yang lebih dari 10 akan berakhir")

# While Dengan BREAK
print("===============WHILE Dengan BREAK===============")
angka = 0
while angka < 10:
    if angka is 5:

        print("statement diatas fungsi break yang akan dieksekusi dan akan keluar dari looping")
        break
        print("statement dibawah fungsi break tidak akan dieksekusi")

    print("nilai angka adalah : ", angka)
    angka += 1
else:
    print("nilai yang lebih dari 10 akan berakhir")

print("akan langsung meloncat kesini karena looping keluar akibat fungsi break")
# CATATAN : yang dieksekusi adalah yang sebelum break

jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? [ya/tidak]")
    if jawab == 'tidak':
        break

print("Total perulagan: " + str(hitung))

# While Dengan CONTINUE
print("===============WHILE Dengan CONTINUE===============")
angka = 0
while angka < 10:
    if angka is 5:
        angka += 1
        continue

    print("nilai angka adalah : ", angka)
    angka += 1
else:
    print("nilai yang lebih dari 10 akan berakhir")

print("ini sudah diluar dari loop")

# CATATAN : Hasil akan melewati angka 5 karena ada tambahan angka += 1. jika tidak dikasih angka += 1 maka fungsi continue akan berjalan terus menerus atau infinity loop

# While Dengan PASS
print("===============WHILE Dengan PASS===============")
angka = 0
while angka < 10:
    if angka is 5:
        pass
    print("nilai angka adalah : ", angka)
    angka += 1
else:
    print("nilai yang lebih dari 10 akan berakhir")

print("ini sudah diluar dari loop")


# PERULANGAN NESTED WHILE
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i % j):
            break
        j = j + 1
    if (j > i/j):
        print(i, " adalah bilangan prima")
    i = i + 1

print("selesai")
