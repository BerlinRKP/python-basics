# TIPE DATA NUMBER
import math
print("===============TIPE DATA NUMBER===============")
# Number adalah tipe data python yang menyimpan nilai numerik. number adalah tipe data yang tidak berubah. ini artinya, mengubah nilai dari sejumlah tipe data akan menghasilkan objek yang baru dialokasikan.

# Tipe data number diantaranya: int(), float(), dan complex()

# Fungsi matematika di tipe data number
print("===============FUNGSI MATEMATIKA===============")
# sebelum menggunakan fungsi matematika, kita akan import terlebih dahulu modul math (kalau pun tidak import, juga tidak masalah)
# Operator Matematika (+, -, /, //, *, **, %)

# fungsi-fungsinya:
# fungsi absolut : abs(x)
# fungsi ceiling  : ceil(x)
# fungsi eksponensial : exp(x)
# fungsi logaritma : log(x) dan log10()
# fungsi maximal : max()
# fungsi minimal : min()
# fungsi pangkat : pow(x, y)
# fungsi round (pembulatan kebawah jika < 0.5) : round()
# fungsi kuadrat : sqrt()
# fungsi trigonometri : sin(), cos(), tan(), radians(), dll


# konstanta
print("pi = ", math.pi)
print("e = ", math.e)

# fungsi pangkat
print(math.pow(3, 2))

# fungsi akar kuadrat
print(math.sqrt(9))

# fungsi logaritma
print(math.log(9))

# fungsi trigonometri
print(math.sin(math.radians(90)))

# fungsi absolut
print(abs(-10))
print(abs(10))

# fungsi ceiling : untuk membulatkan kebawah
print(math.ceil(-5.25))
print(math.ceil(5.25))
print(math.ceil(5.75))

# fungsi eksponensial
print(math.exp(1))
print(math.exp(-1))

# fungsi lainnya dilanjutkan

# Fungsi khusus acak : biasa digunakan untuk aplikasi permainan, simulasi, pengujian, keamanan, dan privasi. diantaranya:
# fungsi choice untuk item acak dari list, tuple, atau string : choice(seq)
# fungsi randrange untuk elemen yang dipilih secara acak dari jangkauan : randrange([start,]stop[,step])
# fungsi random : random()
# fungsi untuk menetapkan nilai awal integer yang digunakan dalam menghasilkan bilangan acak. panggil fungsi ini sebelum memanggil fungsi modul acak lainnya. tidak ada pengembalian : seed([])
# fungsi floor untuk nilai dasar dari x, dan int terbesar tidak lebih besar dari x : floor()
# fungsi uniform untuk sebuah float acak r, sedemikian rupa sehingga x kurang dari atau sama dengan r dan r kurang dari y : uniform(x,y)
