# FUNGSI REKURSI DAN LAMDBDA

print("===============1. FUNGSI REKURSI===============")
# Fungsi rekursi adalah fungsi yang memanggil dirinya sendiri secara berulang. Jadi di dalam tubuh fungsi kita memanggil fungsi itu sendiri

# CONTOH. Di dalam matematika, kita mengenal tentang faktorial. Faktorial adalah perkalian bilangan asli berturut – turut dari n sampai dengan 1. Faktorial n dinotasikan dengan n! dimana n! = n (n – 1)(n – 2)(n – 3) ... (3)(2)(1). Faktorial adalah contoh dari fungsi rekursi

# Contoh fungsi rekursi
# Menentukan faktorial dari bilangan


def faktorial(x):
    """Fungsi rekursi untuk menentukan faktorial bilangan"""
    if x == 1:
        return 1
    else:
        return (x * faktorial(x-1))


bil = 4
print("Faktorial dari", bil, " adalah", faktorial(bil))

# Pada contoh di atas, fungsi faktorial() memanggil dirinya sendiri secara rekursi. Ilustrasi proses dari fungsi di atas adalah seperti berikut:
# faktorial(4)
#4 * faktorial(3)
#4 * 3 * faktorial(2)
#4 * 3 * 2 * 1
#4 * 3 * 2
#4 * 6
# 24
# CATATAN : Rekursi fungsi berakhir saat bilangan sudah berkurang menjadi 1. Ini disebut sebagai kondisi dasar (base condition). Setiap fungsi rekursi harus memiliki kondisi dasar. Bila tidak, maka fungsi tidak akan pernah berhenti (infinite loop)

# Keuntungan Menggunakan Rekursi:
# 1.Fungsi rekursi membuat kode terlihat lebih clean dan  elegan
# 2.Fungsi yang rumit bisa dipecah menjadi lebih kecil dengan rekursi
# 3.Membangkitkan data berurut lebih mudah menggunakan rekursi ketimbang menggunakan iterasi bersarang

# Kerugian Menggunakan Rekursi
# 1.Terkadang logika dibalik rekursi agak sukar untuk diikuti
# 2.Pemanggilan rekursi kurang efektif karena memakan lebih banyak memori
# 3.Fungsi rekursi lebih sulit untuk didebug

print("===============2. FUNGSI LAMBDA===============")
# Salah satu fitur python yang cukup berguna adalah fungsi anonim. Dikatakan fungsi anonim karena fungsi ini tidak diberikan nama pada saat didefinisikan

# Pada fungsi biasa kita menggunakan kata kunci def untuk membuatnya, sedangkan fungsi anonim ini kita menggunakan kata kunci lambda. Oleh karena itu, fungsi anonim ini dikenal juga dengan fungsi lambda

# Format Fungsi Lambda:
# Lambda argument : expression

# Fungsi lambda bisa mempunyai banyak argumen, tapi hanya boleh memiliki satu ekspresi. Ekspresi tersebutlah yang dikembalikan sebagai hasil dari fungsi. Fungsi lambda bisa kita simpan di dalam variabel untuk digunakan kemudian


# Program menggunakan lambda 1 argumen
def kuadrat(x): return x*x


# Output: 9
print(kuadrat(3))


# Lambda dengan 2 argumen
def kali(x, y): return x*y


# Output: 12
print(kali(4, 3))

# Penggunaan Fungsi Lambda
print("===============Pengguna Fungsi Lambda===============")
# Lambda digunakan pada saat kita membutuhkan fungsi anonim untuk saat yang singkat. Di Python, fungsi lambda sering digunakan sebagai argumen untuk fungsi yang menggunakan fungsi lain sebagai argumen seperti fungsi filter(), map(), dan lain-lain

print("===============Pengguna Fungsi Lambda dengan Fungsi filter()===============")
# Fungsi filter mengambil dua buah argumen, yaitu satu buah fungsi dan satu buah list
# Sesuai dengan namanya filter (penyaring), fungsi akan menguji  semua anggota list terhadap fungsi, apakah dan mengambil hasil yang bernilai True. Hasil keluarannya adalah sebuah list baru hasil filter. Berikut adalah contohnya:


# Filter bilangan ganjil dari list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_ganjil = list(filter(lambda x: x % 2 != 0, my_list))


# Output: [1, 3, 5, 7, 9]
print(list_ganjil)


print("===============Pengguna Fungsi Lambda dengan Fungsi map()===============")
# Fungsi map() mengambil dua buah argumen, yaitu satu buah fungsi dan satu buah list.

# Fungsi map() akan memetakan atau memanggil fungsi dengan satu persatu anggota list sebagai argumennya. Hasilnya adalah list baru hasil dari keluaran fungsi terhadap masing-masing anggota list. Berikut adalah contohnya:


# Program untuk menghasilkan kuadrat bilangan
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kuadrat = list(map(lambda x: x*x, my_list))

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
print(kuadrat)
