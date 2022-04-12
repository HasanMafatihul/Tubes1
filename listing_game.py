def urutan(list,y,z):
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
    list1 = []
    list2 = []
    for i in range(jumlah-1):
        list1 += [int(list[i][y])]
        list2 += [int(list[i][y])]

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
                list_index += [j]
    
    return list_index

def load_csv(cd):
    global jumlah
    with open (cd) as x:
        lines = x.readlines()

    # mengolah tabel di csv menjadi data
    jumlah = 0
    for i in lines:
        jumlah += 1

    data = ["" for i in range(1, jumlah)]
    for i in range(1, jumlah):
        data [i-1] = lines[i]


    # menjadikan data sebuah matriks
    data1 = [["" for i in range(7)] for j in range(jumlah - 1)]

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
        text1 =""
        for j in text:
            if j != "\n":
                text1 += j
        data1[i][6] = text1
    return data1

data = load_csv('D:\VS code\TUBES DASPRO\game.csv')
skema = input("Skema sorting : ")
if skema == "tahun-" or skema == "tahun+" or skema == "harga-" or skema == "harga+":
    if skema == "tahun-":
        y = 5
        z = "-"
    elif skema == "tahun+":
        y = 5
        z = "+"
    elif skema == "harga-":
        y = 3
        z = "-"
    elif skema == "harga+":
        y = 3
        z = "+"
    list_index = urutan(data, y, z)
    for i in list_index:
        print(f'{data[i][0]} | {data[i][1]} | {data[i][2]} | {data[i][3]} | {data[i][4]} | {data[i][5]} | {data[i][6]}')
elif skema == "":
    for i in range(jumlah-1):
        print(f'{data[i][0]} | {data[i][1]} | {data[i][2]} | {data[i][3]} | {data[i][4]} | {data[i][5]} | {data[i][6]}')
else:
    print("Skema sorting tidak valid!")
