"""
    Perulangan
"""


"""
    For
    For termasuk sintaks dalam Python yang bersifat definite iteration. 
    Definite itertion adalah sebuah proese iterasi atau perluangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.

    format dari perulangan
    for <var> in <iterable>:
        <statement(s)>
"""


var_list = [1,2, 3, 4, 5, 6, 7]

for i in var_list :
    print(i)
 

"""
    Perluangan berdasarakan panjang suatu nilai dengan menggunakan fungsi  "range()".

    range(strat,stop,step)
    start -> nilai awal dari urutan yang bersifat opsi
    stop -> nilai batas yang wajib dimasukan 
    step -> merupakan nilai penambahan natara dua bilangan dalam urutan yang bersifat opsi, jiak tidak dikasihkan secara default adalah 1.
"""

for i in range(10):
    print(i)

for i in range(1, 10, 2) :
    print(i)



"""
    While
    Merupakan sintaks Python bersifat indefinite itertion. indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondidis tertentu.

    format perulangan while : 
    whlie kondisi :
        #blok pernyataan yang akan diulang selama kondisi bernilai true
"""

counter  = 1
while counter <= 5 : 
    print(counter)
    counter += 1 #increment


"""
    For Bersarang
    Nasted Loop / Perulangan dalam perulangan
    Format dari nasted loop  : 

    for variabel_luar in iterable_luar :
        for variable_dalam in iterable_dalam :
            # blok pernytaan yang akan di ulang

"""

for i in range(1, 3) :
    for j in range(1, 3) :
        print(i, j)



"""
    Kontrol Perulangan
    #Break 
    adalah statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perlulangan selanjutnya.
"""

for i in range(2) : 
    print("Perulangan luar : ", i)
    for j in range(10) : 
        print("Perulangan dalam : ", j)
        if j == 1 : 
            break # Menghentika perilangan jiak j = 1


for huruf in 'Dico ding' : 
    if huruf == ' ' :
        break
    print('Huruf saat ini : {}'.format(huruf))


"""
    Continue
    adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continou seolah mengabaikan pernytaan (statement) yang berada anatra continou hingga akhir blok
"""

for huruf in 'Dico ding' :
    if huruf == ' ':
        continue 
    print('Huruf saan ini : {}'.format(huruf))

"""
    Else setelah For
    Berfungsi untuk perulangan oencarian. Else setelah for iini bisa dikatakn sebagai memberikan jalan keluar program saat pencarian tidak di temukan
"""

numbers = [1, 2, 3, 4, 5]

for num in numbers :
    if num == 6 :
        print("Angka di temukan! Program berhenti")
        break
else : 
    print("Angka tidak di temukan!")




"""
    Else setelah While
    Berbeda dengan else setelah for, pada statement else setelah while, blok statement esle akan selalu disesekusi saat kondisi pada while menjadi salah.
"""

count =  0
while count < 3 :
    print("Dicoding")
    count += 1
else :
    print("Blok else diesksekusi karena pada while salah (3<3 == false)")




n = 10
while n > 0 : 
    n = n - 1
    if n == 7 : 
        break
    print(n)
else : 
    print("Loop selsesai")




"""
    Pass statement adalah pernyataan yang digunakan jika adna menginginkan sebuah perntaan atau blok pernyataan (statemet), tetapi tidak ada tindakan atau program tidak melakukan apa pun
"""


x = 20
if x > 5 : 
    pass
else :
    print("Nilai x tidak ditemukan")



"""
    List Comprehension
    Masih terkait perulangan, terkadang ada kalanya kita oerlu membuat sebuah list baru berdasarkan list yang sudah ada
"""

angka = [1, 2, 3, 4]
pangkat = []

for n in angka : 
    pangkat.append(n**2)
print(pangkat)


angka = [1, 2, 3, 4 ]
pangkat = [n**2 for n in angka]
print(pangkat)


























