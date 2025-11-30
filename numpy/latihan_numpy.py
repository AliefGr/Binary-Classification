import sys
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
var_list = [[1,2,3], [4,5,6], [7,8,9]]
print(matriks)

print("Ukuran keseluruhan elemen list dalam bytes = ", sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen Numpy dalam bytes = ", matriks.size*matriks.itemsize)


matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]

print(matriks)


matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)

"""
    Mengakses element matriks
"""

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[2][1])


"""
    Oprasi Matriks
    Dua Matriks seklasigus ataupun dua sekligus sja 
"""

# Oprai satu matrix
"""
    - Menghitung total semua elemen matriks.
    - Mengalikan elemen matriks dengan konstanta
    - Transpose matriks
    - Invers MatriksMenentukan determen dan sebagianya.
"""


#Oprasi dua matriks
"""
    - Menambahkan dua Matriks.
    - Mengalikan dua matriks.
    - Pembagian dua matriks, dan sebgianya.
"""


#membuat matriks 2x2
var_mat = [[5, 0],
            [1, -2]]
def_math = [[0 for j in range(2)] for i in range(2)]
print(def_math)

for i in range(len(var_mat)) :
    print("Ini var math = ", var_mat)
    for j in range(len(def_math)) :
        print("def math = ", def_math)
        def_math[i][j] = var_mat[i][j]*2

print(def_math)





