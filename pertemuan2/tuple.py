#Tuple adalah kumpulan yang terurut dan tidak dapat diubah
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apel", "pisang", "mangga", "jeruk")
print(len(thistuple))

# Tuple dengan 1 item (benar)
thistuple = ("apple",)
print(thistuple)
print(type(thistuple))

# Bukan tuple (salah)
thistuple2 = ("apple")
print(thistuple2)

tuple1 = ("apple", "banana", "cherry")   # tuple berisi string
tuple2 = (1, 5, 7, 9, 3)                 # tuple berisi integer
tuple3 = (True, False, False)            # tuple berisi boolean

print(tuple1)
print(tuple2)
print(tuple3)

thistuple = tuple(("apple", "banana", "cherry"))  # double round-brackets
print(thistuple)
print(type(thistuple))

thistuple = ("apel", "pisang", "mangga", "jeruk")
print(thistuple[2])

thistuple = ("apel", "pisang", "mangga", "jeruk")

print(thistuple[0])   # item pertama
print(thistuple[-1])  # item terakhir

# Tuple utama
thistuple = ("apel", "pisang", "mangga", "jeruk", "kiwi", "melon", "anggur")

# 1. Ambil item dari index 2 sampai sebelum index 5
print("1.", thistuple[2:5])

# 2. Ambil item dari awal sampai sebelum index 4
print("2.", thistuple[:4])

# 3. Ambil item dari index 3 sampai akhir
print("3.", thistuple[3:])

# 4. Ambil item dengan index negatif (-5 sampai sebelum -2)
print("4.", thistuple[-5:-2])

thistuple = ("apel", "pisang", "mangga", "jeruk")

# Cek apakah "apel" ada di dalam tuple
if "apel" in thistuple:
    print("Ya, 'apel' ada di dalam tuple buah")

# Cek apakah "anggur" ada di dalam tuple
if "anggur" in thistuple:
    print("Ya, 'anggur' ada di dalam tuple buah")
else:
    print("Tidak, 'anggur' tidak ada di dalam tuple buah")

