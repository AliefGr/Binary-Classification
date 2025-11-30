


class Mobil : 
    def __init__(self, warana, merek, kecepatan) :
        self.warana = warana
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self) :
        self.kecepatan += 10



class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

#Kelas Dasar Mobil 
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

#Kelas Mobil MobilSport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print((mobil_sport_1.kecepatan))
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)


"""
    Override
    membuat metode baru di kelas turunan (kelas baru) dengan nama yang sama seperti metode di kelas induk, itu akan menyebabkan metode baru menimpa (override) metode dari kelas induk.
"""

class Motor :
    def __init__(self, warana, merek, kecepatan) :
        self.warana = warana
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 20

class MotorSport(Motor) :
    def turbo(self):
        self.kecepatan += 50
    def tambah_kecepatan(self):
        self.kecepatan += 20


#kelas motro sport 
motor_sport_1 = MotorSport("Hitam", "Honda", 160)
print(motor_sport_1.kecepatan)
motor_sport_1.tambah_kecepatan()
print(motor_sport_1.kecepatan)


"""
    Super
    Lantas, bagaimana cara untuk kita ingin menggunakan metode atau atribut dari kelas induk, tetapi tidak ingin menuliskan ulang semua kode? Ini adalah tujuan dari adanya super dalam konsep OOP. Nama super sebenarnya merujuk pada kelas induk yang disebut juga sebagai super class. Kita bisa memanfaatkan konsep ini untuk menghindari kode berulang dan memanfaatkan fungsi yang sudah ada pada kelas induk (super class).
"""

class Sepeda :
    def __init__(self, warana, merek, kecepatan) :
        self.warana = warana
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10 


class SepedaSport(Sepeda):
    def turbo(self) :
        self.kecepatan += 50

    def tambah_kecepatan(self) :
        super().tambah_kecepatan()
        print("Kecepatan betambah, Hati-hati")

sepeda_1 = SepedaSport("Hijau", "Poligon", 160)
print(sepeda_1.kecepatan)
sepeda_1.tambah_kecepatan()
print(sepeda_1.kecepatan)






