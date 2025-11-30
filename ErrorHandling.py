var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    
"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
"""
