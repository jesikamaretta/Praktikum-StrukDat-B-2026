#digunakan untuk menyimpan nilai data dalam pasangan kunci:nilai
mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(mobil)


mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(mobil["brand"])


mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(mobil)


mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(mobil))


data_mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "aktif": True,
    "hobi": ["membaca", "coding"]
}

print(data_mahasiswa)


mobil = dict(brand="Ford", model="Mustang", year=1964)

print(mobil)


mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(mobil.keys())


mobil = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

kunci = mobil.keys()

mobil["color"] = "red"

print(kunci)
