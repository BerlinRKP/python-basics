# TIPE DATA TUPLE
print("===============TIPE DATA TUPLE===============")
# Tuple merupakan struktur data yang digunakan untuk menyimpan sekumpulan data seperti list, akan tetapi data yang sudah terisi dalam tuple tidak bisa diubah dan dihapus. sebuah tuple dibuat dengan () dan dipisah dengan koma (,).

# Tuple bersifat immutable yang artinya isi tuple tidak bisa diubah dan dihapus, namun bila anggotanya adalah tuple bersarang dengan anggotanya terdapat list, maka item pada dilist tersebut dapat diubah

tuple1 = (1, 2, 3, "hallo", "dunia", "python")

# khusus tuple yang mempunyai satu nilai cara penulisannya tetap harus ada koma untuk menunjukan bahwa itu tuple
tuple_satu_nilai = ("satu nilai",)

# Mengakses Indek dan Pengirisan Tuple
print("===============Mengakses Indek dan Pengirisian Tuple===============")
print(len(tuple1))
print(type(tuple1))
print(tuple1[0])
print(tuple1[1:4])

# Tuple Nested : tuple dalam tuple
print("===============Tuple Nested===============")
tuple2 = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
tuple3 = (1, 2, 3, 4, 5, 6, 7)
tuple_nested = (tuple2, tuple3)
print("ini adalah tuple nested : ", tuple_nested)
print(len(tuple_nested))
print(tuple_nested[0][0])

# Tuple mampu menampung objek berbagai tipe data seperti list, dictonary, dll. dan ketika dalam penampungan terdapat bersarang seperti list, maka list tersebut bisa diubah nilainya
print("===============Tuple Menampung Berbagai Tipe Data===============")
tuple4 = ([1, 2, 3], False)
print(len(tuple4))
print(type(tuple4))
print(tuple4[0][2])
# mengubah nilai list dalam tuple
tuple4[0][:] = 3, 2, 1
print(tuple4)

# Catatan
# Operator Tuple (+) dan (*) = sama seperti list
# Fungsi Tuple = seperti list
