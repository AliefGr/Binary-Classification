print("Hallo World")

# Input

name = input('masukan nama anda : ')
print(name)

print(type(name))

# type data Integer
x = 7
print(type(x))

#type data float
z = 3.14
print(type(z))

#type data complex
y = 1+2j

print(type(y))

"""
    type data number bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah
"""

var = 10
print(var)
print(id(var))

var = 11
print(var)
print(id(var))

# Boolean
# true & false

x = False
z = True
print(type(x))
print(type(z))

# string

x = "Dicoding"
print(type(x))

multiLIne = """ Hallo nama saya alief gymnastiar saya seorang. """
print(multiLIne)

# String merupakan urutan karakter yang setiap karekternya memiliki indeks

x = "Dicoding"
print(x[0])

"""
    Namaun tidak bisa mengubah substring di dalamnya
    x[0] =  "Z"

    Output:
    TypeError: 'str' object does not support item assignment

    kita daoat mengakses beberapa substring dengan menggunakan metode slice dan indexing
"""

x = "Dicoding"
print(x[2:])    
#output coding

name = "Alief"
print(f"Hello, nama {name}")
# print("Hallo nama saya" % {name});


"""
Type data colection
"""

#list

x = [1, 2, 3, "Dicoding"]

print(type(x))
print(x[1])


"""
    List di Python berdifat mutable yang artinya nilinya dapat diubah
"""

x[0] = "Alief"
print(x)

x =  ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

# Anda memerintahkan untuk mengambil data dari indeks ke-0 hingga indeks ke-4 dengan setiap elemen ke-2 dan kelipatannya akan dilewati
print(x[0:5:2])
# Pada sintaks kedua, Anda memerintahkan untuk menampilkan data dari indeks ke-1 hingga terakhir.
print(x[1:])
#  Pada sintaks ketiga, Anda memerintahkan untuk menampilkan data dari indeks ke-0 hingga indeks ke-2 (ingat, bersifat eksklusif).
print(x[:3])

# tuple

x = (1, 2, "alief")
print(type(x))

print(x[2])

"""
    Tuple bersifat immutable yang artinya tidak dapat diubah.  
    x[2] = "dicoding"


    Output :
    'tuple' object does not support item assignment

"""


""" 
    SET

    Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.

"""

x = {1, 2, 7, 9, 17, 19}
print(x)


""" 
    Dictinary   
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x)
print(type(x))
print(x['name'])
# Ganti data
x['name'] = "Alief"
print(x)

#nambah data
x["job"] = "Web Dev"

# hapus data dictionary
del x["isMarried"]

print(x)


"""
    Koversi Integer ke float 
"""

print(float(5))

"""
    Koversi float ke Integer
"""
print(int(5.6))
print(int(-5.6))

"""
    Konversi dan ke string
"""
print(float("4.5"))


# Koversi Kumpulan Tipe Data
print(set([1,2,3]))
print(list('hello'))
print(tuple({2,3,3}))









































































