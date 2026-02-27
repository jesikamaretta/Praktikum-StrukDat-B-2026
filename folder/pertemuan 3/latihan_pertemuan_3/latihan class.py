class Person:
    def __init__(self,nama,status,mimpi):
        self.nama = nama
        self.status = status
        self.mimpi = mimpi

    def panggil_nama(self):
        print(f"nama saya {self.nama}")
        
    def panggil_status(self):
        print(f"status saya{self.status}")

person1 = Person("jeyu", "mahasiswa", "mysawit") 
person2 = Person("jane", "mahasiswa", "mybrondolan") 
person3 = Person("anas", "pekerja", "mykawan")

print(person1.nama, person1.status, person1.mimpi)
print(person2.nama, person2.status, person2.mimpi)
print(person3.nama, person3.status, person3.mimpi)

person1.status = "pekerja"



