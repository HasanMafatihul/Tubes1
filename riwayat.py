def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x        
def tambah(li,x):
    li += [x]
def hapus(li,x):
    sama = False
    list = []
    i = 0
    while sama == False:
        if li[i] == x:
            sama = True
        else:
            i +=1
    for j in range(banyak(li)):
        if j != i:
            list += [li[j]]
    return list
def banyak_data_csv(cd):
    with open (cd) as x:
        lines = x.readlines()
    jumlah = banyak(lines)
    return jumlah
def load_csv(cd, banyak_kolom, jumlah):
    with open (cd) as x:
        lines = x.readlines()
    # mengolah tabel di csv menjadi data
    data = ["" for i in range(jumlah)]
    for i in range(jumlah):
        data [i] = lines[i]


    # menjadikan data sebuah matriks
    data1 = [["" for i in range(banyak_kolom)] for j in range(jumlah)]

    for i in range(jumlah):
        text = ""
        kolom = 0
        for j in data[i]:
            if j != ";":
                text += j
            else:
                data1[i][kolom] = text
                kolom += 1
                text = ""
        text1 =""
        for j in text:
            if j != "\n":
                text1 += j
        data1[i][banyak_kolom-1] = text1
    return data1
def rapih(data, x, jumlah):
    panjang_string = banyak(data[0][x])
    for i in range(jumlah):
        if panjang_string < banyak(data[i][x]):
            panjang_string = banyak(data[i][x])
    return panjang_string

user_id = "USER003" #didapat dari login misal yang login memiliki user_id USER003
jumlah = banyak_data_csv('TUBES_DASPRO/data/riwayat.csv')
data = load_csv('TUBES_DASPRO/data/riwayat.csv', 5, jumlah)
terpenuhi = False
for i in range(jumlah):
    terpenuhi = False
    for j in range(5):
        if data[i][3] == user_id or data[i][3] != user_id:
            terpenuhi = True
            if j != 3:
                print(data[i][j], end=" ")
                print(" " * (rapih(data, j, jumlah) - banyak(data[i][j])), end="")
                print("|", end="")
    if terpenuhi == True:
        print("")