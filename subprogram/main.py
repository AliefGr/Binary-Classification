from typing import MutableMapping

from numpy import inf, info, result_type
import hello


def menacri_luas_persegi_panjang(panjang, lebar) :
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = menacri_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = menacri_luas_persegi_panjang(4, 20)
print(persegi_panjang_kedua)

"""
    Keyword 
"""

#1. === Keyword argument ===
"""
    Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan.
"""

def mencari_luas_persegi_panjang(panjang, lebar) :
    luas_persegi_panjang = panjang * lebar 
    return luas_persegi_panjang

persegi_panjang_pertama = menacri_luas_persegi_panjang(panjang = 5, lebar=10 )

print(persegi_panjang_pertama)


# Positional Argument 
"""
    Kebalikan dari keyword Positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit.
"""


def menacri_luas_persegi_panjang(panjang, lebar) :
    luas_persegi_panjang  = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = menacri_luas_persegi_panjang(4, 7)


# parameter

#1 Pramater-or-keyword

def greeting(nama, pesan) :
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat Sore!", nama="Dicodng"))

#2 Positional-Only
"""
        Parameter ini hanya dapat dimanfaatkan dengan menggunakan jenis argumen posisi saat pemanggilan fungsi.
"""

def penjumlahan(a ,b, /):
    return a + b

print(penjumlahan(2, 20))
#print(penjumlahan(a = 2, b = 20))


#3 Keyword-Only 

"""
Jenis ketiga adalah kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis parameter ini.
"""

def greeting(*, nama, pesan):
    return "Halo, " + "! " + pesan

print(greeting(pesan="Selamat Sore", nama="Dicodng"))

#4 Var-Positional(Variadic Positional Parameter)

"""
    Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks *args.
"""

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1,2,3))



# Var-Keyword(Variadic Keyword Parameter)

"""
    Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.
"""

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Alief", usia="17", pekrjaan="Developer"))



# Fungsi Anonim (Lambda Expression)
"""
    Terakhir, mari kita pelajari cara membuat fungsi tanpa mendeklarasikan def. Cara ini dikenal dengan ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya. Anda bisa mengasumsikan fungsi anonim ini sebagai fungsi one-liner.
"""


def func(args) :
    return ret_val

#jadi 

func = lambda args : ret_val


mencari_luas_persegi_panjang =  lambda panjang, lebar : panjang * lebar 
print(menacri_luas_persegi_panjang(2,2))



# Variabel Global dan Lokal


"""
Dalam Python, ada konsep "scope" yang mengatur jangkauan variabel dan fungsi dalam suatu program. Konsep ini lebih dikenal sebagai scope variable yang mengacu pada wilayah di dalam program tempat variabel dapat diakses dan digunakan.
"""

#Variabel Global
"""
Suatu variabel yang didefinisikan di luar fungsi atau blok kode apa pun dan dapat diakses dari seluruh bagian program.
"""

a = 10

def add(b):
    result = a + b 
    return result

bilangan_pertama = add(20)
print(bilangan_pertama)


#Variabel Local
"""
    Variabel ini didefinisikan dalam suatu fungsi atau blok kode tertentu. Jenis ini hanya dapat diakses dari dalam fungsi atau blok kode tempat variabel tersebut didefinisikan.
"""

def add(a,b):
    local_var = 5
    result = a + b - local_var
    return result

bilangan_pertama = add(10, 10)
print(bilangan_pertama)



# Menulis Modul pada Python

"""
Pembahasan terakhir terkait fungsi adalah kita akan mempelajari cara memanggil sebuah fungsi dari berkas lain. Masih ingat dengan modul? Ia adalah sebuah file berisi kode Python dan di dalamnya terdapat fungsi, kelas, dan sebagainya.

Sebab setiap file berekstensi .py dapat direferensikan sebagai modul, Anda bisa melakukan impor file dari satu file ke yang lainnya. Layaknya ketika Anda me nggunakan library, modul, dan sebagainya.
"""



persegi_panjang_pertama = hello.menacri_luas_persegi_panjang(7, 2)
print(persegi_panjang_pertama)
