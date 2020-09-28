# PERCABANGAN
print("===============PERCABANGAN===============")
# Percabangan merupakan suatu program untuk menentuan suatu keputusan sesuai dengan logika/kondisi yang berikan
# nama lain percabangan diantaranya control flow, decision, struktur kondisi
# pada python ada beberapa statemen/kondisi diantaranya adalah if, if else, if elif else
# materi percabangan, dalam pengambilan keputudan yang ada di kondisi bisa menggunakan seluruh operasi yang ada di python, sesuai dengan kebutuhannya

# Kondisi if
print("===============Kondisi if===============")
# kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar/True, sedangkan jika kondisi bernilai salah/False maka statement/kondisi tidak akan dieksekusi
kondisi = 1
if(kondisi > 10):
    print("Selamat Anda Lulus")

if(kondisi < 10):
    print("Selamat Anda Juga Lulus")

# Kondisi if else
print("===============Kondisi if else===============")
# Pengambilan keputusan (kondisi if else) tidak hanya digunakan untuk menentukan tindakan apa yang akan diambil sesuai dengan kondisi, tetapi juga digunakan untuk menentukan tindakan apa yang akan diambil/dijalankan jika kondisi tidak sesuai

# Kondisi if else adalah kondisi dimana jika pernyataan benar True maka kode dalam if akan dieksekusi, tetapi jika bernilai salah False maka akan mengeksekusi kode di dalam else
angka = 1
if(angka > 5):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")

# Kondisi if elif else
print("===============Kondisi if elif else===============")
# Pengambilan keputusan (kondisi if elif) merupakan lanjutan/percabangan logika dari “kondisi if”. Dengan elif kita bisa membuat kode program yang akan menyeleksi beberapa kemungkinan yang bisa terjadi. Hampir sama dengan kondisi “else”, bedanya kondisi “elif” bisa banyak dan tidak hanya satu
hari = str(input("kamu memilih hari apa?"))
if(hari == "senin"):
    print("saya memakai seragam putih abu-abu"),
elif(hari == "selasa"):
    print("saya memakai seragam putih abu-abu"),
elif(hari == "rabu"):
    print("saya memakai seragam putih abu-abu"),
elif(hari == "kamis"):
    print("saya memakai seragam batik"),
elif(hari == "jumat"):
    print("saya memakai seragam pramuka"),
elif(hari == "sabtu"):
    print("saya memakai seragam olahraga"),
elif(hari == "minggu"):
    print("saya ngopi di lembayung"),
else:
    print("anda salah menginput hari")


nilai = int(input("Inputkan nilaimu: "))

if nilai >= 90 and nilai <= 100:
    dapat = "A"
elif nilai >= 80 and nilai < 90:
    dapat = "B+"
elif nilai >= 70 and nilai < 80:
    dapat = "B"
elif nilai >= 60 and nilai < 70:
    dapat = "C+"
elif nilai >= 50 and nilai < 60:
    dapat = "C"
elif nilai >= 40 and nilai < 50:
    dapat = "D"
elif nilai >= 0 and nilai < 40:
    dapat = "E"
else:
    dapat = "Input Nilai Salah dan harus 1 - 100"

print("nilai kamu %d maka mendapat : %s " % (nilai, dapat))


# Kondisi if bersarang (Nested if)
print("===============Kondisi if bersarang (Nested if)===============")
# jika suatu kondisi if terpenuhi maka bisa menambah syarat lagi di dalamnya untuk pengambilan keputusan statement/kondisi yang lebih spesifik atau mendalam
# if (kondisi):
#       if(kondisi):
#           -perintah yang dieksekusi jika kondisi terpenuhi-
# atau:
# if (kondisi):
#   if(kondisi):
#       -perintah yang dieksekusi jika kondisi terpenuhi-
#   else:
#       -perintah yang dieksekusi jika kondisi terpenuhi-
# else:
#   -perintah yang akan dieksekusi jika kondisi terpenuhi-

# catatan : pada nested if ini, tingkat bersarang nya tidak hanya dua, tetapi bisa berapa saja sesuai dengan kebutuhan

kelulusan = str(input("apakah anda lulus SMA? [ya/tidak] : "))
kota = str(input("pilih kota? [yogyakarta/jakarta/bandung] : "))
universitas = str(input("pilih universitasmu? "))

if kelulusan == "ya":
    print("selamat anda bisa melanjutkan ke perguruan tinggi")
    if kota == "yogyakarta":
        pilih = "silakan anda bisa melanjutkan universitas di yogyakarta"
        if universitas:
            kampus = "selamat anda sudah terdaftar di" + universitas
    elif kota == "jakarta":
        pilih = "silakan anda bisa melanjutkan universitas di jakarta"
        if universitas:
            kampus = "selamat anda sudah terdaftar di" + universitas
    elif kota == "bandung":
        pilih = "silakan anda bisa melanjutkan universita di bandung"
        if universitas:
            kampus = "selamat anda sudah terdaftar di" + universitas
    else:
        pilih = "kota yang anda pilih tidak masuk kriteria"
else:
    print("maaf, anda tidak bisa melanjutkan ke perguruan tinggi karena belum lulus")

# Kondisi if untuk list
print("===============Kondisi if untuk list===============")
pelajaranipa = ["Matematika", "Kimia", "Biologi", "Fisika", "Bahasa"]
pelajaranips = ["Sosiologi", "Sejarah", "Ekonomi", "Bahasa"]
pilih = "Matematika"

if pilih in pelajaranipa:
    print("anda memilih pelajaran", pilih)
else:
    print("tidak ada pelajaran", pilih)
