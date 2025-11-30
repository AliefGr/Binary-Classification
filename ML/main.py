import pandas as pd 

tesData = pd.read_csv('test.csv', dtype={26: str, 27: str})

print(tesData.head())

"""
Pertama-tama, mari kita periksa tipe data dari masing-masing fitur yang ada di dataset. Tujuan dari pemeriksaan tipe data ini adalah untuk memastikan seluruh tipe data yang ada sudah sesuai dan tidak ada kekeliruan (contoh: data numerik terdeteksi str (string)). Sehingga, pada akhirnya Anda tidak akan mengalami kesulitan ketika melakukan preprocessing data karena tipe data yang ada sudah sesuai dan bisa melalui proses dengan lebih seamless.
"""
print(tesData.info())


"""
Dengan melakukan analisis statistik deskriptif, kita bisa memastikan bahwa data yang digunakan untuk melatih model machine learning adalah data yang representatif, berkualitas tinggi, dan bebas dari masalah yang dapat memengaruhi hasil akhir. Berikut adalah contoh kode untuk melakukan analisis deskriptif.
"""
print(tesData.describe(include="all"))

"""
Terakhir Anda perlu melakukan pemeriksaan terhadap data yang hilang (missing value). Tujuannya untuk mencegah kesalahan ketika melakukan analisis, mencegah error pada model, dan meningkatkan performa model. Dengan melakukan pemeriksaan missing value, Anda dapat memastikan bahwa proses analisis data dan pelatihan model machine learning berjalan dengan baik sehingga hasil yang diperoleh lebih valid dan akurat. Berikut salah satu contoh kode untuk melakukan pemeriksaan missing value.
"""

## Memeriksa jumlah nilai yang hilang di setiap kolom

missing_value = tesData.isnull().sum()
print(missing_value[missing_value > 0 ])

"""
Pertama-tama, mari kita pisahkan kolom yang memiliki missing value lebih dari 75% dan kurang dari 75%.
"""

less = missing_value[missing_value < 1000].index
over = missing_value[missing_value >= 1000].index


# Contoh mengisi nilai yang hilang dengan median untuk kolom numerik

numeric_feature = tesData[less].select_dtypes(include=['number']).columns

tesData[numeric_feature] = tesData[numeric_feature].fillna(tesData[numeric_feature].median())

"""
Secara singkat kode di atas memiliki dua fungsi utama yaitu sebagai berikut.

Baris pertama memilih nama-nama kolom dari DataFrame train yang memiliki tipe data numerik dari subset kolom yang ditentukan oleh less.

Baris kedua kemudian mengisi semua nilai yang hilang (NaN) pada kolom-kolom numerik tersebut dengan nilai median dari masing-masing kolom.

Secara keseluruhan, kode ini bertujuan untuk membersihkan data dengan memastikan bahwa semua kolom numerik dalam subset tertentu (train[less]) tidak memiliki missing value (NaN) dengan menggantinya menggunakan nilai median kolom masing-masing.
"""

# Contoh mengisi nilai yang hilang dengan mode untuk kolom kategori
kategorical_features = tesData[less].select_dtypes(include='object').columns


for column in kategorical_features:
    tesData[column] = tesData[column].fillna(tesData[column].mode()[0])

"""
Kode di atas akan melakukan pengulangan pada setiap kolom yang berisi data kategori dalam DataFrame train. Selanjutnya, setiap kolom kategori akan melakukan proses pergantian untuk semua nilai yang hilang (NaN) dengan nilai modus dari kolom tersebut. Hasil akhirnya adalah semua kolom kategori dalam DataFrame train tidak lagi memiliki nilai yang hilang (NaN) karena semua NaN telah diisi dengan nilai modus dari kolom masing-masing.
"""

# Menghapus kolom dengan terlalu banyak nilai yang hilang
df = tesData.drop(columns=over)

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])


