"""

    
    
"""


score = 100

if score == 100 : print("Nilai anda Sempuran");

"""
    if else
"""

tinggi_badan = 167

if tinggi_badan >= 160 : 
    print("anda boleh menaiki roler soaster")
else :
    print("Anda tidak diperbolehkan")

"""
    elif
    or and
"""
nilai = 90
perilaku = "Tidak Baik"

if nilai >= 80 and perilaku == "Tidak Baik" : 
    print("Selamat anda mendapatkan nilai A dan tapi perilakumu kurang baik")
    print("Pertahankan")
elif nilai >= 80 and perilaku != 'baik' : 
    print("Hore, Anda Mendapatkan nilai B, dan perlukaumu baik sekali")
    print("Tingkatkan")
elif nilai >= 60 :
    print("Hmm... Anda mendpatakan nilai C")
    print("Ayo Semangat!")
else : 
    print("Waduh, Anda Mendaptakan nilai D")
    print("Yuk Belajar Lebih giat lagi!")


lulus = True

print("Selamat") if lulus else print("Pebaiki")


kelulusan = ("Perbaiki, anda belum lulus", "Selamat adana belum lulus")[lulus]

print(kelulusan)














