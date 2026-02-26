kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

#1)Tentukan mata kuliah yang diambil kedua kelas
for x in kelas_A == kelas_B:
    print(x)

    kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

# 1. Mata kuliah yang diambil oleh kedua kelas (irisan)
sama = kelas_A.intersection(kelas_B)

# 2. Mata kuliah yang hanya diambil kelas A (selisih)
hanya_A = kelas_A.difference(kelas_B)

# 3. Seluruh mata kuliah unik (gabungan)
unik = kelas_A.union(kelas_B)

print("Mata kuliah yang diambil kedua kelas:", sama)
print("Mata kuliah yang hanya diambil kelas A:", hanya_A)
print("Seluruh mata kuliah unik:", unik)
