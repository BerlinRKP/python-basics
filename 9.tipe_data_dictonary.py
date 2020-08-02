# TIPE DATA DICTONARY
print("===============TIPE DATA DICTONARY===============")
# Dictonary merupakan struktur data yang anggotanya terdiri dari pasangan kunci:nilai (keys:values). dan dalam kunci tidak boleh ada dua kunci yang sama (unik), sedangkan untuk nilai nya bisa berupa tipe data apapun
# Dictonary bersifat tidak terurut sehingga anggotanya tidak memiliki indeks
# values atau nilai dalam dictonary bersfat mutablem sehingga kita bisa mengubah nya
# membuat dictonary : dict ={"keys":"values"}
# membuat dictonary kosong dengan fungsi dict{}

dict1 = {
    "nama": "setyo dwi pratama",
    "tanggallahir": "14 juni 1996",
    "umur": 22,
    "alamat": "indramayu",
    "kodepos": 123456
}
print(dict1)
print(type(dict1))

# kita juga bisa menggunakan konstruktor dict{}
# khusus kasus ini, sebuah keys tidak boleh diawali dengan angka
dict2 = dict(a1="merah",
             a2="kuning",
             a3="hijau",
             a4="hitam",
             a5="putih"
             )
print(dict2)

# Mengaksis Nilai
print("===============Mengakses Nilai===============")
print(dict1["nama"], dict1["tanggallahir"])
print(dict1.values())  # fungsi values() akan mengambil semua nilai
print(dict1.get("a1"))  # fungsi get() juga untuk mengambil nilai

# Mengubah dan Menambah Nilai
print("===============Mengubah dan Menambah Nilai===============")
# untuk mengubah
dict1["nama"] = "nama baru"
print(dict1)

# untuk menambah
dict1.update({"hobi": "sepakbola", "kontak": "08981938732"})
print(dict1)

# mengubah dengan fungsi update
dict1.update({"hobi": "futsal"})
print(dict1)

# Menghapus Nilai
print("===============Menghapus Nilai===============")

# fungsi del untuk menghapus suatu item (kunci dan nilai dihapus)
del dict1["nama"]
print(dict1)

# fungsi pop untuk menghapus
dict1.pop("tanggallahir")
print(dict1)

# fungsi clear untuk mengapus semua nya
dict1.clear()
print(dict1)

# Fungsi Dictonary
print("===============Fungsi Dictonary===============")
# cmp(dict1,dict2) : untuk membandingkan unsur keduanya
# len(dict) : untuk melihat panjang total dictonary atau jumlah item
# str(dict) : untuk menghasilkan representasi string yang dapat dicetak dari dictonary
# type(variabel) : mengembalikan tipe variabel yang lulus. jika variabel yang dilewatkan adalah dictonary maka akan mengembalikan tipe dictonary

# Metode Dictonary
print("===============Metode Dictonary===============")
# dict.clear() : untuk menghapus semua elemen dictonary
# dict.copy() : untuk menyalin dictonary
# dict.fromkeys() : untuk membuat dictonary baru dengan kunci dari seq dan nilai yang disetel ke nilai
# dict.get(key,default=None) : nilai pengembalian atau default jika tombol tidak ada dalam dictonary
# dict.items() : untuk mengembalikan daftar dari pasangan (key,value)
# dict.keys() : untuk mengembakikan daftar nilai dictonary
# dict.setdefault(key, default=None) : mirip dengan get(), tapi akan mengatur dict[key]=default jika kunci belum ada di dict
# dict.update(dict) : untuk menambah dan mengubah dictonary
# dict.values() : untuk mengembalikan daftar nilai dictonary

# Dictonary dalam dictonary (Nested Dictonaty)
print("===============Nested Dictonary===============")
nested1 = {
    "anak1": {
        "nama": "anggi",
        "umur": 30
    },
    "anak2": {
        "nama": "tyo",
        "umur": 20
    },
    "anak3": {
        "nama": "elsa",
        "umur": 10
    }
}

print(type(nested1))
print(nested1)

# atau
anak1 = {
    "nama": "anggi",
    "umur": 30
}
anak2 = {
    "nama": "tyo",
    "umur": 20
}
anak3 = {
    "nama": "elsa",
    "umur": 10
}

nested1 = {
    "anak1": anak1,
    "anak2": anak2,
    "anak3": anak3
}
print(nested1)
print("nested1: %d" % len(nested1))
