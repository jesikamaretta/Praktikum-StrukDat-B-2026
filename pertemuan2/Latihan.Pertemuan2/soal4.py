mahasiswa = {
    "A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

# 1. Nama mahasiswa dengan IPK di atas 3.5
print("Mahasiswa dengan IPK di atas 3.5:")
for nim, data in mahasiswa.items():
    if data["ipk"] > 3.5:
        print(data["nama"])

# 2. Hitung rata-rata IPK seluruh mahasiswa
total_ipk = 0
jumlah = 0

for data in mahasiswa.values():
    total_ipk += data["ipk"]
    jumlah += 1

rata_ipk = total_ipk / jumlah
print("Rata-rata IPK:", rata_ipk)

# 3. Tambahkan data mahasiswa baru
mahasiswa["A004"] = {"nama": "Rina", "prodi": "Teknik Komputer", "ipk": 3.60}

print("Data mahasiswa setelah ditambah:")
print(mahasiswa)


