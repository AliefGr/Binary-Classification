#Transformasi Angka, Krakter, dan String

#Mengubah Huruf Besar/Kecil

"""
    upper()
    Mengubah Huruf Kecil Ke Kecil
"""

kata = "dicoding"
kata = kata.upper()
print(kata)

"""
    lower()
    Mengubah Huruf Besar Ke Kecil
"""
kata = "DICODING"
kata = kata.lower()
print(kata)

# Awalan Dan Akhiran

"""
    rstrip()
    Metode ini menghapus whitespace pada sebuah kanan atau akhir string.
"""

print("Dicoding        ".rstrip())

"""
    lstrip()
    Metode in menghapus whitespace pada sebuah kiri string.
"""

print("               Dicoding".lstrip())


"""
    strip()
    Metode ini bertugas untuk menghapus whitespace awal dan akhir
"""
print("     Dicoding     ".strip())


"""
    startswith()
    Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
"""

print('Dicoding Indonesia'.startswith('Dicoding'))


"""
    endswith()
    Metode endswith() bertujuan untuk menemukan suatu kata di akhir ini juga mengembalikan nilai True.
"""
print("Decoding Indonesia".endswith('Dicodinf'))



#    Memisah dan Mengabung String
"""
    Join()
    Mengabung string
"""

print(' '.join(["Dicoding", "Indonesia"]))































