# OPERATOR BITWISE
print("===============OPERATOR BITWISE===============")
# Operator Bitwise adalah operator khusus untuk menangani operasi logika bilangan biner dalam bentuk bit
# untuk memanggil bilangan biner kita menggunakan fungsi bin() : bin(1), bin(123456789), dan seterusnya
# bilangan biner sendiri merupakan jenis bilangan yang hanya terdiri 2 jenis angka (0 dann 1), sedangkan desimal memiliki (0,1,2,3,4,5,6,7,8,9)

x = 10  # dikonversi ke biner jadi 1010
y = 12  # dikonversi ke biner jadi 1100

print('x berisi angka', x, 'desimal atau', bin(x), 'biner')
print('y berisi angka', y, 'desimal atau', bin(y), 'biner')

print('\n')

print('nama operator and, x & y  :', x & y)
print('nama operator or, x | y  :', x | y)
print('nama operator xor, x ^ y  :', x ^ y)
print('nama operator not, ~x :', ~x)
print('nama operator left shift, x << 1 :', x << 1)
print('nama operator right shift, x >> 1 :', x >> 1)

# dalam contoh diatas, telah didefinisikan 2 variabel x dan y. dan memberikan nilai awal 10 dan 12, jika dikonversikan dalam bentuk biner keduanya berisi angka berikut:
# x = 10 (desimal) = 1010 (biner)
# y = 12 (desimal) = 1100 (biner)
# Di baris 4 dan 5 saya menggunakan function bawaan python, yakni bin(), ini bisa dipakai untuk menampilkan versi biner dari sebuah angka desimal. Awalan 0b merupakan penanda bahwa ini adalah angka biner. Artinya, angka 0b1010 adalah 1010 dalam bilangan biner
# Operator bitwise pertama adalah operasi & (And) terhadap kedua variabel. Operasi bitwise “and” ini akan memproses bit per bit dari kedua variabel, jika kedua bit sama-sama 1, maka hasilnya juga 1, selain kondisi tersebut, nilai akhirnya adalah 0. Berikut perhitungan bitwise “and”:
# x =     1010
# y =     1100
# x & y = 1000 = 8 (desimal)
# Operator bitwise kedua adalah operasi | (Or), hasilnya akan bernilai 0 jika kedua bit bernilai 0, selain itu nilai bit akan di set menjadi 1. Berikut cara perhitungan bitwise “or”:
# x =     1010
# y =     1100
# x | y = 1110 = 14 (desimal)
# Operator bitwise ketiga adalah operasi ^ (Xor), hasilnya akan bernilai 1 jika salah satu dari kedua variabel bernilai 1 (namun tidak keduanya). Atau dengan kata lain jika kedua bit berlainan, hasilnya 1 tapi kalau sama-sama 0 atau sama-sama 1, hasilnya 0
# x =     1010
# y =     1100
# x ^ y = 0110 = 6 (desimal)
# Selanjutnya adalah operasi ~ atau not, yang akan membalikkan nilai bit sebuah variabel dari 0 menjadi 1, dan 1 menjadi nol. Namun perhitungan bit not ini sedikit membingungkan karena jika kita hanya membalikkan seluruh bit saja, hasilnya tidak sesuai dengan apa yang dihitung Python:
# x =     1010
# ~x =    0101 = 5 (desimal) ==> salah??
# dari hasil menjalankan program, dapat dilihat bahwa hasilnya ~x = -11, dari mana bisa hasilnya -11?
# Ini berkaitan dengan cara bahasa python menyimpan angka biner (dan juga hampir semua bahasa pemrograman komputer modern). Angka biner di dalam bahasa python disimpan dalam format “Two’s complement”. Penjelasan tentang “Two’s complement” ini cukup panjang, jika tertarik saya sudah membahasnya lengkap di buku Pascal Uncover, atau bisa ke Two’s complement Wikipedia.
# Secara singkat, rumusnya adalah -x - 1, sehingga ~x = -10 - 1 = -11(desimal)
# Operator bitwise selanjutnya adalah operator shift left, dimana nilai variabel x akan digeser sebanyak 1 digit ke kiri:
# x      = 1010  = 10
# x << 1 = 10100 = 20 (desimal)
# Ketika hasil pergeseran ke kiri, digit paling kanan akan diisi angka 0. Setiap penggeseran 1 tempat ke kiri akan mengkali 2 nilai asal. Karena variabel x berisi desimal 10, maka hasil dari << 1 sama dengan 10 * 2 = 20
# dan yang terakhir operasi shift right, dimana bahasa python akan menggeser posisi bit dalam variabel x ke kanan sebanyak 1 tempat. Berikut proses yang terjadi:
# x      = 1010 = 10
# x >> 1 =  101 = 5 (desimal)
# Operator shift right menggeser nilai biner variabel x ke arah kanan, sehingga digit paling kanan akan dihapus. Operator shift right ini akan menghasilkan nilai asal / 2. Dalam contoh kita, hasilnya adalah 10/2 = 5 (dibulatkan)
