# __init__ selalu dieksekusi saat objek diinisiasi (dibuat)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
print('------')
class Car:
    def __init__(self, merek, warna, tahun):
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    def klakson(self):
        print("Tit tit titt")

mobil1 = Car("Toyota", "Hitam", 2022)
mobil1.klakson()