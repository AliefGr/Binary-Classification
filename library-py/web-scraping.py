from urllib.request import urlopen
from bs4 import BeautifulSoup

"""

Beautifulsoup
Beautifulsoup adalah library untuk mengambil data dari halaman web dan mengekstrak informasi yang diperlukan. Untuk menggunakan beautifulsoup, Anda harus menginstalnya terlebih dahulu. Silakan jalankan kode pip berikut untuk menginstalnya.
pip install beautifulsoup4


"""


# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)



"""

Urllib
Urllib adalah library bawaan dari Python yang bertujuan untuk scraping konten dari sebuah website. Penggunaan urllib berbeda dengan beautifulsoup. Bisa dikatakan bahwa cara penggunaan urllib sedikit kompleks dibandingkan beautifulsoup. Kode di bawah adalah contoh untuk memulai proses scraping pada situs dengan domain python.org dan menampilkan isi dari tag title dari situs tersebut.

"""

from urllib.request import urlopen
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
 
# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)


name = "Perseus Evans" 
print(name)

"""
x = 'Dicoding'
x[0] = 'F'
print(x)

"""

print(dict([['name','Dicoding'],['age',17]]))

lulus = True 
print("Dicoding Indonesia") if lulus else print("Python")
