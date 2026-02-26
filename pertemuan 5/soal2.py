kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)] 
#Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75, tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, tampilkan: "Maaf us remidi." 

for i in kumpulan_nilai:
    if i[1] >= 75:
        print(f"Selamat{i[0]}, Anda Lulus")
    else:
        print(f"Maaf{i(0)}, Anda Tidak Lulus")