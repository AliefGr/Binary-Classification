
"""
    Disarankan
"""
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

"""
    Tidak disarankan seperti ini.
"""
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

"""
    Anda diperbolehkan untuk membuat sebuah konten/isi dari if/for/while yang cukup pendek untuk diletakkan dalam satu baris (program tetap berjalan). Namun, pastikan tidak melakukannya jika if/for/while Anda bertingkat atau bersifat multi clause, misalnya if-else, try-finally, dan sebagainya.
"""
# Tidak disarankan seperti ini.
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

# Sangat tidak Disarankan
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()
try: something()
finally: cleanup()
do_one(); do_two(); do_three(long, argument,
                             list, like, this)
if foo == 'blah': one(); two(); three()


"""
    Penggunaan Trailing Commas
    Koma di bagian akhir (trailing commas) umumnya bersifat opsional, satu statement yang bersifat wajib adalah saat kita membuat variabel menggunakan tipe tuple dengan satu elemen. Hal ini umumnya diperjelas dengan kurung untuk menghindari penghapusan atau pembersihan.
"""
# Disarankan seperti ini.
FILES = ('setup.cfg',)
#Tidak disarankan seperti ini.
FILES = 'setup.cfg',

"""
    Saat trailing comma bersifat redundan, Anda akan merasakan kemudahannya saat menggunakan VCS (Version Control System), atau pada kode yang mungkin ditambahkan dalam beberapa waktu ke depan. Pola yang disarankan adalah meletakkan nilai atau string pada sebuah baris baru, mengikuti indentasi, menambahkan trailing comma, dan menutup kurung/kurawal/siku pada baris selanjutnya.

    Tidak umum jika Anda menempatkan trailing comma pada baris letak Anda menutup kurung/kurawal/siku seperti di bawah ini, kecuali dalam tuple dengan satu elemen, seperti yang dijelaskan di atas.
"""

#disarankan
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
#tidak disarankan
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)


"""
  Anotasi Fungsi
Anotasi fungsi adalah fitur yang memungkinkan kita untuk menambahkan informasi tambahan tentang parameter dan return value dari sebuah fungsi. Jika sebelumnya kita belajar menambahkan informasi terkait fungsi dengan menambahkan docstring, anotasi fungsi lebih spesifik untuk menjelaskan parameter dan return value.

Penggunaan anotasi fungsi sebaiknya menggunakan aturan baku untuk titik dua (:) dan menggunakan spasi untuk penggunaan arah panah atau arrow (->). Hal ini disebut sebagai type hints yang merujuk pada PEP 484.  
"""

def persegi_panjang(panjang: int = 2, lebar: int = None):
    luas = panjang*lebar
    return luas

luas_persegi_panjang = persegi_panjang(lebar=2)
print(luas_persegi_panjang)



""" 
    Namun, perlu diingat bahwa karena type hints bersifat optional dan memberikan petunjuk, jika pada fungsi LuasPersegiPanjang kita memberikan tipe data float, program akan tetap berjalan sebagaimana mestinya. 

    Sekarang, kita masuk ke skenario baru. Jika pada saat membuat fungsi tanpa adanya anotasi bahwa parameternya menandakan keyword argumen atau nilai default, hindari penggunaan spasi di sekitar tanda sama dengan (=).
"""


Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas

""" 
    Mari kita simpulkan sedikit. Jika kita membuat fungsi yang menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi sebelum dan sesudah tanda sama dengan (=). Namun, ketika membuat fungsi biasa tanpa adanya anotasi, sebaiknya tidak menggunakan spasi sebelum dan sesudah tanda sama dengan (=). 
"""

Yes:
def LuasPersegiPanjang(panjang:int = 2, lebar=None):
    pass
 
No:
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass
