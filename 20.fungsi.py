# FUNGSI
print("===============FUNGSI===============")
# Fungsi adalah grup/blok program untuk melakukan tugas tertentu yang berulang. Fungsi membuat kode program menjadi reusable, artinya hanya di definisikan sekali saja, dan kemudian bisa digunakan berulang kali dari tempat lain di dalam program. Fungsi memecah keseluruhan program menjadi bagian – bagian yang lebih kecil . Dengan semakin besarnya program, maka fungsi akan membuatnya menjadi lebih mudah diorganisir

# sintak fungsi:
# def function_name(parameters):
#    """function_docstring"""
#    statement(s)
#    return [expression]

# Penjelasannya dari sintaks fungsi di atas:
# 1. Kata kunci def diikuti oleh function_name (nama fungsi), tanda kurung dan tanda titik dua (:) menandai header (kepala) fungsi
# Parameter / argument adalah input dari luar yang akan diproses di dalam tubuh fungsi
# "function_docstring" bersifat opsional, yaitu sebagai string yang digunakan untuk dokumentasi atau penjelasan fungsi. “function_doctring” diletakkan paling atas setelah baris def
# Setelah itu diletakkan baris – baris pernyataan (statements). Jangan lupa indentasi untuk menandai blok fungsi.
# return bersifat opsional. Gunanya adalah untuk mengembalikan suatu nilai expression dari fungsi


# membuat fungsi1
def fungsi1():
    print("ini adalah bagian-bagian untuk statement")


# memanggil fungsi1
fungsi1()
fungsi1()
fungsi1()

# Fungsi dengan Parameter
print("===============Fungsi dengan Parameter===============")
# Format fungsi dengan parameter

# def nama_fungsi(parameter):
#    print parameter


# membuat fungsi2
def fungsi2(angka):  # saat membuat parameter, tipe data dapat disesuaikan
    print(angka)


# memanggil fungsi2
fungsi2(123456)


# membuat fungsi3
def fungsi3(angka1, angka2):
    tambah = angka1 + angka2
    print("angka1 + angka2 = ", tambah)


# memanggil fungsi3
fungsi3(2, 2)


#Fungsi yang Mengembalikan Nilai
print("===============Fungsi yang Mengembalikan Nilai===============")
#Format fungsi yang mengembalikan nilai

#def nama_fungsi(parameter):
#    balikfungsikesini = a + b
#    return(balikfungsikesini)

