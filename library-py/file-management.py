import os
import json
import pickle

print(os.getcwd())

"""

OS
Modul OS pada Python berguna untuk fungsi-fungsi yang berkaitan dengan sistem operasi, misalnya open(), path(), getcwd(), dan fungsi lainnya. Modul ini memungkinkan Anda untuk memanfaatkan fungsi yang sama dan mengeksekusi fungsi terkait OS yang mungkin berbeda dalam setiap sistem operasi. Ada beberapa fitur yang hanya bekerja pada sistem operasi tertentu.


"""



# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
 
# parse  x:
y = json.loads(x)

print(y)
print(y["umur"])


"""

Pickle
Jika Anda memiliki sebuah list yang ingin disimpan atau ditransmisikan tanpa khawatir bentuknya akan rusak atau kacau, fungsi dari library pickle dapat dimanfaatkan. Pickle termasuk fungsi Object Serialization pada Python. Pickling adalah istilah untuk mengubah objek menjadi byte stream, sedangkan unpickling adalah perlakuan sebaliknya.

"""

import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()


pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)
