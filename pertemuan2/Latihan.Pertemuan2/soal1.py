angka = [10, 20, 30, 40, 50]
#1)tambahkan angka 60 ke dalam list
angka.append(60)
print(angka)

#2)hapus angka 20
angka = [10, 20, 30, 40, 50]
angka.remove(20)
print(angka)

#3)tampilkan angka tertinggi dan terendah
angka = [10, 20, 30, 40, 50]
max = 10
min = 50
print(max, min)


angka = [10, 20, 30, 40, 50]

# 1. Tambahkan angka 60
angka.append(60)

# 2. Hapus angka 20
angka.remove(20)

# 3. Tampilkan angka tertinggi dan terendah
tertinggi = max(angka)
terendah = min(angka)

print("Angka tertinggi:", tertinggi)
print("Angka terendah:", terendah)

# 4. Hitung rata-rata setelah perubahan
rata_rata = sum(angka) / len(angka)
print("Rata-rata:", rata_rata)

# 5. Tampilkan seluruh isi list
print("Isi list setelah perubahan:", angka)
