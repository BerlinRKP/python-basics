# OPERATOR IDENTITAS DAN KEANGGOTAAN
print("===============OPERATOR IDENTITAS DAN KEANGGOTAAN===============")
# kedua operator ini juga disebut operator khusus (spesial operator), karena tidak selalu tersedia di bahasa pemograman lain

# OPERATOR IDENTITAS
print("===============OPERATOR IDENTITAS===============")
# Operator Identitas adalah operator yang digunakan untuk memeriksa apakah nilai sebuah variabel ada di tempat yang sama atau tidak
# is : bernilai True jika kedua nilai merujuk ke objek yang sama dan berisi nilai yang sama
# is not : bernilai True jika kedua nilai merujuk ke objek yang tidak sama
a = 5
b = 5
c = 6
print('a is b :', a is b)
print('a is c :', a is c)
print('a is not c :', a is not c)
print('\n')

i = 'setyo dwi pratama'
j = 'setyo dwi pratama'
print('i is j :', i is j)
print('i is not j :', i is not j)
print('\n')

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print('x is y :', 'a' is y)
print('x is not y :', x is not y)

# Untuk tipe data dasar seperti number atau string, jika dua buah variabel berisi nilai yang sama, maka operator is akan menghasilkan nilai True.
# Namun dalam contoh terakhir, variabel x dan y berisi tipe data list. Meskipun nilai element-nya sama persis, tapi Python menyimpannya di alamat memory yang berbeda, sehingga dianggap tidak identik. Hasilnya, x is y adalah False.


# OPERATOR KEANGGOTAAN
print("===============OPERATOR KEANGGOTAAN===============")
# Operator keanggotaan adalah operator yang dipakai untuk memeriksa apakah suatu nilai ada di dalam sebuah himpunan atau tidak. Himpunan yang dimaksud terdiri dari tipe data “berbentuk array” seperti string, list, tuple, set dan dictionary. Operator ini dikenal juga sebagai membership operators.
# in : bernilai True jika nilai yang dicari ada di dalam himpunan
# not in : bernilai True jika nilai yang dicari tidak ada di dalam himpunan
anggota = 'Belajar Python'
print('anggota :', anggota)
print('\'B\' in anggota :', 'B' in anggota)
print('\'b\' not in anggota :', 'b' not in anggota)
print('\'B\' not in anggota :', 'B' not in anggota)
print('\n')


abjad = ['a', 'b', 'c']
print('abjad :', abjad)
print('\'a\' in abjad   :', 'a' in abjad)
print('\'a\' not in abjad :', 'a' not in abjad)
print('\'d\' not in abjad :', 'd' not in abjad)
print('\n')

angka = (12, 43, 102, 55)
print('angka :', angka)
print('102 in anjad     :', 102 in abjad)
print('102 not in abjad :', 102 not in abjad)
print('35 not in abjad  :', 35 in abjad)
