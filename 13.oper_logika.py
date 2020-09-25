# OPERATOR LOGIKA
print("===============OPERATOR LOGIKA===============")
# Operator Logika adalah operator yang digunakan untuk membuat suatu kesimpulan logis dari 2 kondisi boolean (True atau False). python memiliki 3 operator logika yaitu and, or dan not

print('Hasil dari True and True   :', True and True)
print('Hasil dari True and False  :', True and False)
print('Hasil dari False and True  :', False and True)
print('Hasil dari False and False :', False and False)

print('\n')

print('Hasil dari True or True   :', True or True)
print('Hasil dari True or False  :', True or False)
print('Hasil dari False or True  :', False or True)
print('Hasil dari False or False :', False or False)

print('\n')

print('Hasil dari not True  :', not True)
print('Hasil dari not False :', not False)

print('\n')
# operator logika juga dapat dilakukan dalam berbagai kondisi untuk menghasilkan kesimpulan logis
hasil = (5 > 6) and (10 <= 8)
print(hasil)

hasil = ('python' == 'python') or (10 <= 8)
print(hasil)

hasil = not (10 < 10)
print(hasil)

hasil = ('duniailkom' == 'duniailkom') and (10 <= 8) or (1 != 1)
print(hasil)

# operasi yang akan dijalankan dimulai dari kiri terlebih dahulu, kita juga bisa menggunakan () untuk memprioritaskan apa yang harus dijalankan terlebih dahulu
