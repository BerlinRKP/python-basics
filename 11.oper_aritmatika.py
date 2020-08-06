# OPERATOR ARITMATIKA
print("===============OPERATOR ARITMATIKA===============")
# Operator Aritmatika adalah operator yang biasa ditemukan untuk operasi matematika. aritmatika merupakan cabang ilmu matematika yang membahas perhitungan sederhana.
a = 10
b = 5
print("operator penjumlahan + : ", a+b)
print("operator pengurangan - : ", a-b)
print("operator perkalian * : ", a*b)
print("operator pembagian / : ", a/b)
print("operator pembagian dibulatkan kebawah // : ", a//b)
print("operator modulus % : ", a % b)
print("operator pemangkatan ** : ", a**b)

# selain operator diatas, operator aritmatika juga memiliki 2 jenis unary yaitu + dan -
c = +1
d = -2
print("c-d =", c-d)

# Priorita Operator Aritmatika
prioritas1 = 10 + 6 * 2 + 2
print(prioritas1)

# dari contoh diatas operasi perkalian akan dijalankan terlebih dahulu sesuai konsep dalam matematika, sehingga ketika ingin operasi mana terlebih dahulu yang mau kita jalankan maka harus menggunakan ()
prioritas2 = (10 + 6) * (2 + 2)
print(prioritas2)
