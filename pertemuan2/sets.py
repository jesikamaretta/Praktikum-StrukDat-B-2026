#ururtan jgn dihiraukan
thisset1 = {"apple", "banana", "cherry", "apple"}
print("Set 1:", thisset1)

# True dan 1 dianggap sama
thisset2 = {"apple", "banana", "cherry", True, 1, 2}
print("Set 2:", thisset2)

# False dan 0 dianggap sama
thisset3 = {"apple", "banana", "cherry", False, True, 0}
print("Set 3:", thisset3)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Set dengan tipe data string
set1 = {"apple", "banana", "cherry"}
print("Set String:", set1)

# Set dengan tipe data integer
set2 = {1, 5, 7, 9, 3}
print("Set Integer:", set2)

# Set dengan tipe data boolean
set3 = {True, False, False}
print("Set Boolean:", set3)

# Set campuran beberapa tipe data
set4 = {"apple", 10, True, 3.14}
print("Set Campuran:", set4)


# Membuat set menggunakan set() constructor
thisset = set(("apple", "banana", "cherry"))  # double round brackets
print("Set hasil constructor:", thisset)

# Membuat set dari list (menghapus duplikat)
mylist = ["apple", "banana", "apple", "cherry"]
newset = set(mylist)
print("Set dari list:", newset)

# Membuat set dari string
text = "hello"
settext = set(text)
print("Set dari string:", settext)

thisset = {"apple", "banana", "cherry"}

# Loop untuk menampilkan semua item dalam set
print("Isi set:")
for x in thisset:
    print(x)

# Mengecek apakah item tertentu ada di dalam set
if "banana" in thisset:
    print("\nYa, 'banana' ada di dalam set")
else:
    print("\nTidak, 'banana' tidak ada di dalam set")

# Mengecek item lain
if "mango" in thisset:
    print("Ya, 'mango' ada di dalam set")
else:
    print("Tidak, 'mango' tidak ada di dalam set")


thisset.add("orange")



# Menambahkan item dari set lain menggunakan update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print("Hasil update dari set:", thisset)


# Menambahkan item dari list menggunakan update()
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print("Hasil update dari list:", thisset)


# 1. remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print("Set setelah remove():", thisset)


# 2. discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print("Set setelah discard():", thisset)


# 3. pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("Item yang dihapus dengan pop():", x)
print("Set setelah pop():", thisset)


# 4. clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("Set setelah clear():", thisset)


# 5. del
thisset = {"apple", "banana", "cherry"}
del thisset

# print(thisset)  # ini akan error karena set sudah dihapus
print("Set sudah dihapus dengan del")



thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

