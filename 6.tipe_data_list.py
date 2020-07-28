# TIPE DATA LIST
print("===============TIPE DATA LIST===============")
# List merupakan struktur data yang mampu menyimpan lebih dari satu data seperti array. sebuah list dibuat dengan [] dan pemisahnya koma(,)

# list bersifat mutable yang artinya isinya bisa kita ubah-ubah

list1 = [1, 1.1, "string"]
print(list1)
print(type(list1))

# Akses Indek List dan pengirisan
print("===============Akses Indek List===============")
print(list1[0])
print(list1[2])
print(list1[:1])
print(list1[1:])

# Update Nilai List
print("===============Update Nilai List===============")
# list dapat memperbarui satu atau beberapa nilai dengan memberikan potongan di sisi kiri operator penugasan kemudian menambahkan nilai ke dalam list dengan metode apppend()
list1[2] = "Hello World!"
print("update nilai indek ke 2 : ", list1[2])
print(list1)

# Hapus Nilai List
print("===============Hapus Nilai List===============")
# dalam menghapus nilai didalam list, dapat menggunakan salah satu pernyataan del() jika tahu persis elemen yang aka dihapus. metode remove() jika tidak tahu persis item mana yang akan dihapus. fungsi pop() seklain untuk menghapus elemen list juga mengembalikan nilai indeks elemen tersebut (hal ini berguna ketika ingin memanfaatkan indeks dari elemen yang terhapus untuk digunakan kemudian). dan fungsi clear() untuk mengosongkan list
list2 = [1, 2, 3, 4, 5]
print("list awal sebelum dihapus : ", list2)

list2.remove(1)
print("fungsi remove : ", list2)

del(list2[0:2])
print("fungsi delete : ", list2)

list2.clear()
print("fungsi clear : ", list2)

# Operasi Pada List
print("===============Operasi Pada List===============")
list3 = [10, 20, 30, 40, 50]
list4 = [60, 70, 80, 90, 100]

print("Fungsi Length: ", len(list3))
print("Fungsi Penjumlahan: ", list3 + list4 + list1)
print("Funsi Perkalian: ", list3 * 2)
print("Fungsi Membership: ", 10 in list3)  # akan menghasilkan nilai boolean

# Fungsi List
print("===============Fungsi List===============")
# len(list) : melihat panjang list
# max(list) : melihat nilai maksimal
# min(list) : melihat nilai minimal
# list(seq) : mengubah tuple menjadi list

# Metode List
print("===============Metode List===============")
# beberapa metode list:

buah = ["apel", "mangga", "jeruk", "manggis"]

# list.count(objek) : melihat jumlah pada list

# list.append(objek) : menambahkan objek dari belakang ke list
buah.append("semangka")
print("fungsi append : ", buah)

# list.prepend(objek) : menambahkan objek dari depan ke list

# list.extend(seq) : menambahkan isi seq ke list
buah.extend(["tambah satu", "tambah dua"])
print("fungsi extend : ", buah)

# list. index(objek) : mengambil indek list

# list.insert(index, objek) : menambahkan objek ke dalam list di indeks tertentu
buah.insert(1, "anggur")
print("fungsi insert : ", buah)

# list.remove(objek) : menghapus objek dari list
buah.remove("anggur")
print("fungsi remove : ", buah)

# list.reverse() : membalikan suatu list
buah.reverse()
print("fungsi reverse : ", buah)

# list.sort([func]) : mengurutkan objek list
buah.sort()
print("fungsi sort : ", buah)
# atau
buah = sorted(buah)
print("ini juga fungsi sort", buah)


# List Multidimensi
print("===============List Multidimensi===============")
# list multidimensi biasanya digunakan untuk menyimpan struktur data yan kompleks seperti tabel, matriks, graph, dan lainnya

list_multi = [
    ["bakso", "sate", "mie ayam"],
    ["thai tea", "es campur", "jus buah"],
    [100, 200, 300]
]

print(type(list_multi))
print(len(list_multi))
print(list_multi)
print(list_multi[2][2])

# List Dalam List (Nested List)
list_dalam_list = ["anggur", [1, 2, 3], "apel"]
print(list_dalam_list)
# bandingkan hasilnya dengan list multidimensi ketika mengakses indeknya
print(len(list_dalam_list))
print(list_dalam_list[1][0])

# List Comprehension
ls3 = [[i, i**2] for i in range(10) if i % 2 == 0]
print(ls3)
