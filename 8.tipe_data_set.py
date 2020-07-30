# TIPE DATA SET (HIMPUNAN)
print("===============TIPE DATA SET===============")
# Set merupakan tipe data yang berisi kumpulan tipe data dan dipakai untuk mengolah himpunan (set). jika dibandingkan dengan tipe data berbentuk array lain di python, tipe data set berbeda dalam hal index, pengurutan dan keunikan nilai
# tipe data set tidak memiliki indek, sehingga tidak ada mekanisme pengurutan dan tidak bisa menambah nilai baru ke dalam tipe data set dengan cara menulis nomor indek. akan tetapi kita bisa menambahkan sebuah nilai dalam data set dengan menggunakan fungsi add atau update
# tipe data set juga tidak bisa menerima nilai ganda, setiap nilai di dalam set harus unik. jika menginputkan beberapa nilai yang sama, maka hanya satu yang  tersimpan dalam set
# sebuah set dibuat dengan tanda kurung kurawal {} dengan pemisah setiap nilai nya dengan koma (,)
# karena indek tidak bisa dilakukan, maka ketika kita panggil berdasarkan indek nya akan menghasilkan error
# untuk membuat set kosong dengan menggungankan fungsi set()

set1 = {"hallo", "hallo", "dengan", "python", 3, True}
print(set1)  # hasilnya: nilai ganda menjadi hanya satu yang dicetak, dan pengurutannya tidak sesuai apa yang diinputkan
print(type(set1))
print(len(set1))

# Operasi pada Set
print("===============Operasi pada Set===============")
set2 = {1, 2, 3, 4, 5, 6, 7}
set3 = {6, 7, 8, 9, 10}
print("ini adalah operasi gabungan : ", set2 | set3)
print("ini adalah operasi gabungan juga : ", set2.union(set3))


print("ini adalah operasi irisan : ", set2 & set3)
print("ini adalah operasi irisan juga : ", set2.intersection(set3))

print("ini adalah operasi selisih : ", set2 - set3)
print("ini adalah operasi selisih juga : ", set2.difference(set3))

print("ini adalah operasi komplemen : ", set2 ^ set3)
print("ini adalah operasi komplemen juga : ", set2.symmetric_difference(set3))

# Menambahkan Nilai Dalam Data Set
print("===============Menambah Nilai Dalam Data Set===============")

set1.add(2000)  # fungsi add hanya bisa menambah satu nilai
print("menambah nilai dengan fungsi add : ", set1)

set2.update([8, 9, 10])
print("menambah nilai dengan fungsi update : ", set2)

# Menghapus Nilai Dalam Data Set
print("===============Menghapus Nilai Dalam Data Set===============")

set4 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "a", "b", "c", "d"}
print("ini anggota set : ", set4)

set4.remove(10)  # fungsi remove hanya bisa menghapus satu nilai
print("menghapus dengan fungsi remove : ", set4)

set4.discard("a")  # fungsi discard hanya bisa menghapus satu nilai
print("menghapus dengan fungsi discard : ", set4)


# Fungsi Pada Set
print("===============Fungsi Pada Set===============")
# add() : menambahkan satu anggota ke set
# clear() : menghapus semua anggota set
# copy() : mengembalikan shollow copy dari set
# difference() : mengembalikan set baru berisi selisih dua atau lebih set
# difference_update() : menghapus semua anggota set lain yang ada di set ini
# discard() : menghapus satu anggota dari set
# intersection() : mengembalikkan set baru berisi irisan antara dua atau lebih set
# intersection.update() : menghapus set dengan irisan set bersangkutan dan set lainnya
# isdisjoint() : mengembalikan True jika dua set tidak memiliki irisan
# issubset() : mengembalikan True jika set lain berisi set ini
# issuperset() : mengembalikan True jika set ini berisi set lain
# pop() : menghapus dan mengembalikkan anggota acak dari sebuah set
# remove() : menghapus satu anggota dari set
# symmetric_difference() : mengembalikkan set baru berisi komplemen dari dua set
# symmetric_difference_update() : mengupdate set dengan komplemen dari set ini dan set lainnya
# union() : mengembalikan set baru berisi gabungan dua atau lebih set
# update() : mengupdate set dengan gabungan set ini dan set lainnya
