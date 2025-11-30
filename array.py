import array
from types import NoneType

x = [1,2,3,4,5,6]
print(type(x))

x = array.array("i", [1,2,3,4,5,6,7])
print(x)
print(type(x))


var_list = [1,2,3]
for elemen in var_list :
    print(id(elemen))

print(var_list)


"""
    Mendefinisikan Nilai Default
    <nama_var> = [<default> for in range(<n>)]
"""

var_list = [0 for i in range(10)]

print(var_list)
for i in range(10) :
    var_list[i] = i + 1

print(var_list)

"""
    akses array
"""

print(var_list[0])


"""
    Pemrosesan Sekuensial pada array
"""

var_arr = [1,2,3,4,5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr) :
        next_element = var_arr[next_index]
    else : 
        next_element = None

    print(f"Current element : {current_element}, next element : {next_element}")



