import re
"""
    
 1. String
    String adalah salah satu modul bawaan Python yang tidak perlu dideklarasikan. Pada modul string ada fungsi-fungsi yang dapat dioperasikan pada variabel bertipe string seperti di bawah.
    upper(): Ubah setiap huruf dalam string menjadi huruf kapital. 
    lower(): Ubah setiap huruf dalam string menjadi huruf kecil.
    split(): Pisahkan teks berdasarkan delimiter (karakter pemisah).
    title(): Jadikan setiap awal kata kapital.
    zfill(): Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.

"""

tesString = "dicoding"
tesString.upper()
print(tesString.upper())
print(tesString.lower())
print(tesString.title())
print(tesString.split("i"))
print(tesString.zfill(20))

"""    
2.  Regex
    Regex atau regular expression adalah sebuah cara untuk mencari teks berdasarkan pola tertentu. Umpamanya, ketika ingin mencari sebuah kata dalam kamus, misalnya arti dari kata parsing, kita akan mencari kata tersebut di halaman yang memiliki kata dengan awalan p, lalu pa. Regex bekerja dengan konsep yang sama.

"""

pola= '^a...s$'
string_tes= 'abyss'

hasil = re.match(pola, string_tes)

if hasil: 
    print("Pencarian Berhasil")
else:
    print("Pencarian Gagl")



