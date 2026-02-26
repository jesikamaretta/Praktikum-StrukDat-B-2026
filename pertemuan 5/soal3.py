sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"} 
#a
a = sesi_pagi & sesi_siang
print(a)

#b.data unik

kehadiran = sesi_pagi | sesi_siang
print(kehadiran)

#c.
Union = sesi_siang.union(sesi_pagi)
print(Union)
