import pandas as pd 
import numpy
import matplotlib.pyplot as plt 

import seaborn as sns
import matplotlib.pyplot as plt

"""
    1. Pandas
    Pandas adalah library populer yang digunakan untuk pengelolaan dan analisis data. Library ini menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi, pembersihan, transformasi, dan analisis data dengan mudah dan efisien.
"""

data = {
    'nama' : ['ALief', 'Albert', 'Nizam', 'Alice'],
    'usia' : [20, 19, 22, 23],
    'Pekerjaan' : ['Engineer', 'Teacher', 'Designer', 'Doctor']
}

df = pd.DataFrame(data)

#menampilkan data frame 
print(df)


"""

 2. NumPy
    Library NumPy adalah package fundamental yang sering digunakan untuk scientific computing pada Python. Library ini menyediakan objek array multidimensi, berbagai jenis objek lainnya, seperti masked array dan matrix, dan sebagainya.

"""



matriks = numpy.array([[1,2,3], [4,5,6], [7, 8, 9]])
print(matriks)



"""

Matplotlib
Selanjutnya adalah matplotlibyang merupakan library untuk melakukan visualisasi data. Matplotlib termasuk jenis library eksternal sehingga Anda perlu melakukan instalasi matplotlib terlebih dahulu. Silakan jalankan kode berikut.

"""

 
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
# Membuat plot garis
plt.plot(x, y)
 
# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
 
# Menampilkan plot
plt.show()


"""
Seaborn
Terakhir adalah library seaborn yang termasuk jenis library dengan tujuan untuk visualisasi data sama seperti matplotlib. Bahkan library seaborn dibangun berdasarkan pada library matplotlib.


"""


 
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()
