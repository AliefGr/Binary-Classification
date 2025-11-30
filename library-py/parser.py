import argparse

"""
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', action='store_true', help="Tampilkan Output")

args = parser.parse_args()

if args.output:
    print("Halo. ini merupakam sebuah output dari panggildicoding.py")
"""

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--nama', required=True, help="Masukan nama anda")

args =parser.parse_args()

print("Terimaksih telah menggunakan penggil aku.py"+args.nama)



