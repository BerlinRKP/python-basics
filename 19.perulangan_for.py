# PERULANGAN FOR
print("===============PERULANGAN FOR===============")
# Perulangan for di python untuk memproses sebuah array/himpunan. dengan format:

# variabel = [tipe data : string, list, tuple, set, dict]
# for i in variabel:
#     statement
#     statement
#     dan seterusnya

# dari format diatas, telah didefinisikan sebuah variabel sebagai sebuah array atau himpunan (string/list/tuple/set/dict)
# perulangan for akan dijalankan sebanyak jumlah element yang ada di dalam variabel, dan sepanjang perulangan variabel i akan berisi element yang sedang diproses

# PERULANGAN FOR UNTUK LIST
print("===============PERULANGAN FOR UNTUK LIST===============")
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in angka:
    print(i)

# PERULANGAN FOR UNTUK SET
print("===============PERULANGAN FOR UNTUK SET===============")
angka = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for i in angka:
    print(i)

# PERULANGAN FOR UNTUK STRING
print("===============PERULANGAN FOR UNTUK STRING===============")
abjad = ("abcdefghijklmnopqrstuvwxyz")
for i in abjad:
    print(i)

# PERULANGAN FOR UNTUK DICTONARY
print("===============PERULANGAN FOR UNTUK DICTONARY===============")
dict1 = {
    "nama": "setyo dwi pratama",
    "tanggallahir": "14 juni 1996",
    "umur": 22,
    "alamat": "indramayu",
    "kodepos": 123456
}

for i in dict1.items():
    print(i)

# FUNGSI RANGE PADA PERULANGAN FOR
print("===============FUNGSI RANGE PADA PERULANGAN FOR===============")
# Struktur perulangan di bahasa Python sepintas tidak memungkinkan kita untuk membuat perulangan angka naik, misalnya dari 1, 2, 3, dst. Namun ini bisa dibuat dengan bantuan fungsi atau function range()
for i in range(5):
    print(i)

print("="*20)

for i in range(5, 10):
    print(i)

print("="*20)

for i in range(3, 30, 3):
    print(i)


# FUNGSI RANGE PADA PERULANGAN FOR
print("===============FUNGSI RANGE PADA PERULANGAN FOR===============")

buah = ["anggur", "apel", "mangga", "semangka"]
sayur = ["wortel", "timun", "sawi", "kacangpanjang"]
daftar_belanja = [buah, sayur]

for subdaftarbelanja in daftar_belanja:
    print(subdaftarbelanja)
    for item in subdaftarbelanja:
        print(item)

# FOR Dengan ELSE
print("===============FOR Dengan ELSE===============")

for i in range(0, 10):
    print(i)
else:
    print("angka sudah sampai 10")
# else akan dijalankan ketika dalam looping sudah selesai


# FOR Dengan BREAK
print("===============FOR Dengan BREAK===============")
# break fungsinya untuk mengakhiri sebuah perulangan

# temukan angka 5
for i in range(0, 10):
    print(i)
    if i is 5:
        print("angka ditemukan", i)
        break
else:
    print("angka sudah sampai 10")
# else tidak akan dijalankan dan langsung keluar looping

# FOR Dengan CONTINUE
print("===============FOR Dengan CONTINUE===============")
# continue fungsinya untuk melanjutkan ke step berikutnya

# temukan angka 5
for i in range(1, 10):
    if i is 5:
        print("angka ditemukan", 5)
        continue
    print("nilai : ", i)
else:
    print("angka sudah sampai 10")

# FOR Dengan PASS
print("===============FOR Dengan PASS===============")
# pass fungsinya untuk tidak melakukan apapun

# temukan angka 5
for i in range(1, 10):
    if i is 5:
        print("angka ditemukan", 5)
        continue
    print("nilai : ", i)
else:
    print("angka sudah sampai 10")
