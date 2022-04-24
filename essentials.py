# Fungsi-fungsi esensial python yang dibuat ulang

# Menghitung banyak/panjang suatu hal terkuantifikasi
def banyak(x):
    c = 0
    for i in x:
        c += 1
    return c

def contain(li, x):
    for i in li:
        if x == i:
            return True
    return False

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

def slice_list(l, i, j):
    if j == 0 or j == None:
        j = banyak(l)
    if j < 0:
        j = banyak(l) + j
    o = []
    for x in range(i, j):
        o += [l[x]]
    return o

def slice_str(s, i, j):
    s = slice_list(s, i, j)
    o = ""
    for i in s:
        o += i
    return o

# Pengganti switch statement untuk python
def switch(match, case):
    for i in case:
        if i[0] == match:
            return i[1]
    return None

# Suplementer rapikan_matriks
def longest_arr(data: list, x):
    panjang_string = banyak(data[0][x])
    for i in range(banyak(data)):
        if panjang_string < banyak(data[i][x]):
            panjang_string = banyak(data[i][x])
    return panjang_string

# Merapikan suatu matriks agar bisa mudah diprint
def rapikan_matriks(data: list):
    o = ""
    l = []

    # Buat list string terpanjang di tiap kolom
    for i in range(banyak(data[0])):
        l = l + [longest_arr(data, i)]

    
    for i in range(banyak(data)):
        for j in range(banyak(data[i])):
            o += data[i][j] + (l[j] - banyak(data[i][j]) + 1) * " " + "|"
        o += "\n"
    return o

# Mengurutkan suatu matriks berdasarkan skema tertentu dan kolom tertentu, mengembalikan indeks matriks tersebut yg sudah diurutkan
def urutan(l, y, skema):
    list1 = []
    list2 = []
    for i in range(banyak(l)):
        id_game = ""
        if y != 0:
            list1 += [int(l[i][y])]
            list2 += [int(l[i][y])]
        else:
            list1 += [int(slice_str(l[i][0], 4, 7))]
            list2 += [int(slice_str(l[i][0], 4, 7))]
    
    list_sorted = []
    list_filtered = []
    list_index = []
    if skema == "+":
        while list1:
            minimum = list1[0] 
            for x in list1: 
                if x < minimum:
                    minimum = x
            list_sorted += [minimum]
            list1 = hapus(list1,minimum)
    else: 
        while list1:
            maksimum = list1[0] 
            for x in list1: 
                if x > maksimum:
                    maksimum = x
            list_sorted += [maksimum]
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

def print_perintah(status):
    if status == "admin":
        print("Perintah yang tersedia : \n-> register \n-> tambah_game \n-> ubah_game \n-> ubah_stok \n-> list_game_toko \n-> search_game_at_store \n-> topup \n-> tic_tac_toe \n-> magic_conch \n-> help \n-> save \n-> exit ")
    elif status == "user":
        print("Perintah yang tersedia : \n-> list_game_toko \n-> buy_game \n-> search_my_game \n-> search_game_at_store \n-> riwayat \n-> tic_tac_toe \n-> magic_conch \n-> help \n-> save \n-> exit ")
    else:
        print("Perintah yang tersedia : \n-> login \n-> tic_tac_toe \n-> magic_conch \n-> help \n-> exit")