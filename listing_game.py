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
def urutan(list,y,z,jumlah):
    list1 = []
    list2 = []
    for i in range(1, jumlah):
        id_game = ""
        if y != 1:
            list1 += [int(list[i][y])]
            list2 += [int(list[i][y])]
        else:
            for j in list[i][y]:
                try:
                    int(j)
                    id_game += j
                except ValueError:
                    id_game += ""
            list1 += [int(id_game)]
            list2 += [int(id_game)]
            
    list_sorted = []
    list_filtered = []
    list_index = []
    if z == "+":
        while list1:
            minimum = list1[0] 
            for x in list1: 
                if x < minimum:
                    minimum = x
            tambah(list_sorted,minimum)
            list1 = hapus(list1,minimum)
    elif z == "-": 
        while list1:
            maksimum = list1[0] 
            for x in list1: 
                if x > maksimum:
                    maksimum = x
            tambah(list_sorted,maksimum)
            list1 = hapus(list1,maksimum)
    for i in list_sorted:
        sama = False
        for j in list_filtered:
            if i == j:
                sama = True
        if sama == False:
            list_filtered += [i]

    for i in list_filtered:
        for j in range(banyak(list2)):
            if i == list2[j]:
                list_index += [j+1]
    
    return list_index
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
def print_rapih(list, kolom, data, jumlah):
    for i in list:
        for j in range(kolom):
            print(data[i][j], end=" ")
            print(" " * (rapih(data, j, jumlah) - banyak(data[i][j])), end="")
            print("|", end="")
        print("")

jumlah = banyak_data_csv('TUBES_DASPRO\data\game.csv')
data = load_csv('TUBES_DASPRO\data\game.csv', 7, jumlah)
skema = input("Skema sorting : ")
if skema == "tahun-" or skema == "tahun+" or skema == "harga-" or skema == "harga+" or skema == "":
    if skema == "tahun-":
        kolom = 5
        z = "-"
    elif skema == "tahun+":
        kolom = 5
        z = "+"
    elif skema == "harga-":
        kolom = 3
        z = "-"
    elif skema == "harga+":
        kolom = 3
        z = "+"
    else:
        kolom = 1
        z = "+"
    list_index = [0] + urutan(data, kolom, z, jumlah)
    print_rapih(list_index, 7, data, jumlah)
else:
    print("Skema sorting tidak valid!")
