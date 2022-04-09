import argparse
def load_csv(cd):
    # membuka file csv
    with open (cd) as x:
        lines = x.readlines()

    # mengolah tabel di csv menjadi data
    jumlah = 0
    for i in lines:
        jumlah += 1

    print(jumlah)
    data = ["" for i in range(1, jumlah)]
    for i in range(1, jumlah):
        data [i-1] = lines[i]


    # menjadikan data sebuah matriks
    data1 = [[" " for i in range(6)] for j in range(jumlah - 1)]

    for i in range(jumlah-1):
        text = ""
        kolom = 0
        for j in data[i]:
            if j != ";":
                text += j
            else:
                data1[i][kolom] = text
                kolom += 1
                text = ""

parser = argparse.ArgumentParser(description = '')
parser.add_argument("directory")
args = parser.parse_args()

if (# tidak ada file di directory):
    print(f'Folder "{args.directory}" tidak ditemukan.')
else:
    load_csv(args.directory)