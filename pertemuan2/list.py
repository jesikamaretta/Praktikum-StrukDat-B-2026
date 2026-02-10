buah = ["apel", "mangga", "pisang"]
print(buah)

buah = ["apel", "mangga", "pisang"]
buah[1] = "jeruk"
print(buah)

angka = [1, 2, 2, 3]
print(angka)

data = ["Best", 20, True]
print(data)
#akses indeks positif
nama = ["Ayu", "Budi", "Citra", "Doni"]
print(nama[2])
#akses indeks negatif
angka = [10, 20, 30, 40, 50]
print(angka[-2])

#3. Rentang Index (Slicing)
nilai = [70, 80, 90, 100, 60, 75]
print(nilai[1:4])
#4. Slicing dari Awal (tanpa nilai awal)
buah = ["apel", "mangga", "jeruk", "nanas", "pisang"]
print(buah[:3])
#slicing sampai akhir
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
print(hari[4:])
#rentang indeks negatif
data = ["A", "B", "C", "D", "E", "F", "G"]
print(data[-5:-2])

#ubah item
matkul = ["Struktur Data", "Matematika", "Basis Data"]
matkul[0] = "Pemrograman Dasar"
print(matkul)

# Membuat list awal
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("List awal:", thislist)

# 1. Mengubah satu item (index tertentu)
thislist[1] = "blackcurrant"
print("Setelah ubah index 1:", thislist)

# 2. Mengubah rentang item (index 1 sampai 3 tidak termasuk 3)
thislist[1:3] = ["watermelon", "grape"]
print("Setelah ubah range index 1:3:", thislist)

# 3. Mengganti 1 item dengan 2 item (list bertambah panjang)
thislist[2:3] = ["papaya", "melon"]
print("Setelah mengganti 1 item jadi 2 item:", thislist)

# 4. Mengganti 2 item dengan 1 item (list berkurang panjang)
thislist[1:3] = ["pineapple"]
print("Setelah mengganti 2 item jadi 1 item:", thislist)

# 5. Menyisipkan item menggunakan insert() tanpa mengganti item lain
thislist.insert(2, "strawberry")
print("Setelah insert strawberry di index 2:", thislist)

# Membuat list awal
thislist = ["apple", "banana", "cherry"]
print("List awal:", thislist)

# 1. Menambah item di akhir list dengan append()
thislist.append("orange")
print("Setelah append('orange'):", thislist)

# 2. Menyisipkan item di index tertentu dengan insert()
thislist.insert(1, "grape")
print("Setelah insert(1, 'grape'):", thislist)

# 3. Menambahkan isi list lain dengan extend()
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("Setelah extend(tropical):", thislist)

# 4. Menambahkan iterable lain (tuple) menggunakan extend()
thistuple = ("kiwi", "watermelon")
thislist.extend(thistuple)
print("Setelah extend(thistuple):", thislist)

# Membuat list awal
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print("List awal:", thislist)

# 1. remove() -> menghapus item berdasarkan nilai (hapus kemunculan pertama)
thislist.remove("banana")
print("Setelah remove('banana'):", thislist)

# 2. pop(index) -> menghapus item berdasarkan index tertentu
thislist.pop(2)
print("Setelah pop(2):", thislist)

# 3. pop() -> menghapus item terakhir jika tidak diberi index
thislist.pop()
print("Setelah pop() (hapus item terakhir):", thislist)

# 4. del -> menghapus item berdasarkan index tertentu
del thislist[0]
print("Setelah del thislist[0]:", thislist)

# 5. clear() -> mengosongkan list (list masih ada tapi kosong)
thislist.clear()
print("Setelah clear():", thislist)


thislist = ["apple", "banana", "cherry"]

print("=== 1. Loop menggunakan for ===")
for x in thislist:
    print(x)

print("\n=== 2. Loop menggunakan index (range + len) ===")
for i in range(len(thislist)):
    print("Index", i, "=", thislist[i])

#("\n=== 3. Loop menggunakan while ===")
i = 0
while i < len(thislist):
    print("Index", i, "=", thislist[i])
    i = i + 1

#("\n=== 4. Loop menggunakan list comprehension ===")
[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# 1. Ambil buah yang mengandung huruf "a"
list_a = [x for x in fruits if "a" in x]
print("Buah yang mengandung 'a':", list_a)

# 2. Ambil buah yang bukan "apple"
list_not_apple = [x for x in fruits if x != "apple"]
print("Buah selain apple:", list_not_apple)

# 3. Copy list tanpa kondisi
copy_list = [x for x in fruits]
print("Copy list:", copy_list)

# 4. Membuat list dari range()
angka = [x for x in range(10)]
print("Angka 0-9:", angka)

# 5. Ambil angka yang kurang dari 5
angka_kecil = [x for x in range(10) if x < 5]
print("Angka < 5:", angka_kecil)

# 6. Mengubah semua buah menjadi huruf besar
upper_fruits = [x.upper() for x in fruits]
print("Huruf besar:", upper_fruits)

# 7. Mengisi list dengan nilai yang sama ("hello")
hello_list = ["hello" for x in fruits]
print("Isi hello:", hello_list)

# 8. Mengganti "banana" menjadi "orange"
replace_banana = [x if x != "banana" else "orange" for x in fruits]
print("Ganti banana:", replace_banana)

# 1. Sort alfabet (ascending)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Sort alfabet ascending:", thislist)

# 2. Sort angka (ascending)
angka = [100, 50, 65, 82, 23]
angka.sort()
print("Sort angka ascending:", angka)

# 3. Sort alfabet descending
thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist2.sort(reverse=True)
print("Sort alfabet descending:", thislist2)

# 4. Sort angka descending
angka2 = [100, 50, 65, 82, 23]
angka2.sort(reverse=True)
print("Sort angka descending:", angka2)

# 5. Sort dengan fungsi custom (berdasarkan jarak dari 50)
def myfunc(n):
    return abs(n - 50)

angka3 = [100, 50, 65, 82, 23]
angka3.sort(key=myfunc)
print("Sort berdasarkan jarak dari 50:", angka3)

# 6. Sort case sensitive (huruf besar lebih dulu)
huruf = ["banana", "Orange", "Kiwi", "cherry"]
huruf.sort()
print("Sort case sensitive:", huruf)

# 7. Sort case insensitive (pakai str.lower)
huruf2 = ["banana", "Orange", "Kiwi", "cherry"]
huruf2.sort(key=str.lower)
print("Sort case insensitive:", huruf2)

# 8. Reverse order (membalik urutan list)
huruf3 = ["banana", "Orange", "Kiwi", "cherry"]
huruf3.reverse()
print("Reverse list:", huruf3)
