#1. Variabel
print("===============1. VARIABEL===============") 
# variabel merupakan tempat penyimpanan data atau nilai. dan didalam python sebuah variabel tidak membutuhkan deklarasi variabel sebagaimana dengan bahasa pemograman lainnya
#format : nama_variabel = <nilai>
variabel1 = "Hello World!" #nilai berupa string
varibael2 = 1234567890 #nilai berupa integer
variabel3 = True #nilai berupa bollean
print("Nilai ini berupa string = ", variabel1)
print("Nilai ini berupa angka = ", varibael2)
print("Nilai ini berupa bollean = ", variabel3)

#Menghapus Variabel 
print("===============Menghapus Variabel===============")
variabel4 = "variabel ini akan dihapus dengan fungsi del()"
print(variabel4)
del(variabel4)

#Mengubah nilai variabel
print("===============Mengubah Nilai Variabel===============")
#sepanjang penulisan program, nilai dari sebuah variabel bisa ditimpa dengan nilai lain.
data = "setyo dwi pratama"
print("nilai dalam variabel data awal = ", data)
data = 14061996
print("perubahan nilai variabel data pertama = ", data)
data = False
print("perubahan nilai variabel data kedua = ", data)


#Catatan Variabel : 
#sebuah variabel dalam python bisa diisi dengan berbagai tipe data (string, number, bollean, dll)
#nama sebuah variabel tidak bisa diawali dengan angka
#nama sebuah variabel harus selain keyword dari bahasa python



#2. Tipe Data
print("===============2. TIPE DATA===============")
# cara kita memberitahu komputer untuk mengelompokan data berdasarkan jenis data yang tersimpan dalam variabel. dan setiap jenis tipe data akan memiliki sifatnya masing-masing

#Untuk melihat tipe data pada suatu variabel dengan fungsi : type()

#Jenis-jenis tipe data 
print("===============Jenis Tipe Data===============")
#String, Integer, Float, Complex Number, Boolean, List, Tuple, Set, Dictonary

Data_string = "Memulai dengan Bahasa Python"
print(Data_string)
print(type(Data_string))

Data_integer = 1000
print(Data_integer)
print(type(Data_integer))

Data_float = 1000.5
print(Data_float)
print(type(Data_float))
#kasus untuk float
kasus_float = 1e2 #e merupakan eksponen 10, jadinya 100.0
print(kasus_float)

Data_ComplexNumber = 1j+1
print(Data_ComplexNumber)
print(type(Data_ComplexNumber))
#kasus untuk data komplek
kasus_komplek = complex(1,1)
print(kasus_komplek)
print(type(kasus_komplek))

Data_boolean = False
print(Data_boolean)
print(type(Data_boolean))

Data_list = ["Satu", 2, "Tiga", 4]
print(Data_list)
print(type(Data_list))

Data_tuple = ("Satu", "Dua", "Tiga", "Empat")
print(Data_tuple)
print(type(Data_tuple))

Data_set = {"Apel", "Belimbing", "Ceri", "Durian"}
print(Data_set)
print(type(Data_set))

Data_dictonary = {"1":"Apel", "2":"Belimbing", "3":"Ceri", "4":"Durian"}
print(Data_dictonary)
print(type(Data_dictonary))

#Tambahan : format berikut berlaku untuk semua jenis tipe data
Data_string = "Memulai dengan Bahasa Python"
print("Data : ", Data_string, "- Bertipe :", type(Data_string))


#Konversi atau Casting
print("===============Konversi atau Casting===============")
#untuk merubah dari satu tipe ke tipe lain

#Fungsi-fungsi untuk mengubah/konversi tipe data :
#int() : untuk mengubah menjadi integer
#float() : untuk mengubah menjadi float
#str() : untuk mengubah menjadi string
#bool() : untuk mengubah menjadi boolean
#long() : untuk mengubah menjadi integer panjang
#chr() : untuk mengubah menjadi karakter
#bin() : untuk mengubah menjadi bilangan biner
#hex() : untuk mengubah menjadi bilangan Heksadesimal
#oct() : untuk mengubah menjadi bilangan okta

print("===============Tipe Data Awal Berupa INTEGER===============")
data_int = 10
print("data = ", data_int , ",type =", type(data_int))
#mengkonversi data
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan "False" jika nilai dari int = 0, lainnya akan "True"
print("data = ", data_float , ",type =", type(data_float))
print("data = ", data_str , ",type =", type(data_str))
print("data = ", data_bool , ",type =", type(data_bool))

print("===============Tipe Data Awal Berupa FLOAT===============")
data_float = 9.5
print("data = ", data_float , ",type =", type(data_float))
#mengkonversi data
data_int = int(data_float) #pada kasus float akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan "False" jika nilai dari int = 0, lainnya akan "True"
print("data = ", data_int , ",type =", type(data_int))
print("data = ", data_str , ",type =", type(data_str))
print("data = ", data_bool , ",type =", type(data_bool))

print("===============Tipe Data Awal Berupa BOOLEAN===============")
data_bool = True
print("data = ", data_bool , ",type =", type(data_bool))
#mengkonversi data
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int , ",type =", type(data_int))
print("data = ", data_str , ",type =", type(data_str))
print("data = ", data_float , ",type =", type(data_float))

print("===============Tipe Data Awal Berupa STRING===============")
data_str = "10"
print("data = ", data_str , ",type =", type(data_str))
#mengkonversi data
data_int = int(data_str) #string akan diubah ke interger jika nilai berupa angka, jika berupa karakter maka akan error
data_bool = bool(data_str) #akan "False" jika nilai dari string kosong
data_float = float(data_str) #string akan diubah ke float jika nilai berupa angka, jika berupa karakter maka akan error
print("data = ", data_int , ",type =", type(data_int))
print("data = ", data_bool , ",type =", type(data_bool))
print("data = ", data_float , ",type =", type(data_float))