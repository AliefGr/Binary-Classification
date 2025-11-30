class Mobil :
    #Atribut 
    warna = "Merah"
    

mobil_1 = Mobil()

print(mobil_1.warna)

#merubah atribut kelas
Mobil.warna = "Hijau"

print(mobil_1.warna)


class Motor :
    def __init__(self) :
        self.warna = "Ungu"


motor_1 = Motor()
print(motor_1.warna)

motor_2 = Motor()
print(motor_2.warna)

# Mengubah atribut instance
motor_1.warna = "Orange"
print(motor_1.warna)


class Pesawat :
    def __init__(self, warna, merek, kecepatan) :
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


pesawat_1 = Pesawat('Merah', 'DicodingAir', 160)

print(pesawat_1.warna)
print(pesawat_1.kecepatan)
print(pesawat_1.merek)


"""
Method
"""

def my_decorator(func) :
    def wrapper():
        print("Sebelum fungsi diesksekusi.")
        func()
        print("Setelah fungsi dieskekusi.")
    return wrapper


# Dekorasi fungsi dengan decorator 
@my_decorator 

def say_hello() :
    print("Hello World")


# memanggil fungsi yang sudah didekorsai 
say_hello()

    
"""
    Metode dari Objek (Object Method)
"""

class Motor :
    def __init__(self, warna, merek, kecepatan) :
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self) :
        self.kecepatan += 10 

motor_1 = Motor("Merah", "Dicoding", 160)
print("Sebelum ditemukan  : ")
print(motor_1.kecepatan)

motor_1.tambah_kecepatan() #Memanggil metode tambah_kecepatan

print("Setelah ditambahkan : ")
print(motor_1.kecepatan)


"""
    Metode secara Statis (Static Method)
"""

class Sepeda :
    def __init__(self, merek) :
        self.merek = merek


    @staticmethod
    def intro_sepeda():
        print("Ini adalah metode dari kelas Sepeda")

Sepeda.intro_sepeda()
sepeda_1 = Sepeda("DicodingBike")
sepeda_1.intro_sepeda()


"""
    Metode dari Kelas (Class Method)
"""


class Becak :
    def __init__(self, merek) :
        self.merek = merek

    @classmethod
    def intro_becak(cls):
        print("Ini adalah metode dari kelas becak")

Becak.intro_becak()
becak_1 = Becak("DicodingBecak")
becak_1.intro_becak()




























