import essentials

scheme = ["tahun", "harga", ""]

# Mengeluarkan listing game berdasarkan skema sorting tertentu
def listing(data, role):
    if role != "admin" and role != "user":
        return
    
    l = data[1][1:]
    skema = input("Skema sorting : ")
    if skema[:-1] in scheme:
        if skema[:-1] == "tahun":
            kolom = 3
            z = skema[-1]
        elif skema[:-1] == "harga":
            kolom = 4
            z = skema[-1]
        else:
            kolom = 0
            z = "+"
        list_index = [0] + essentials.urutan(l, kolom, z)
        
        # Filter menggunakan index
        list_filtered = []
        for i in list_index:
            list_filtered += [data[1][i]]
        print(essentials.rapikan_matriks(list_filtered))
    else:
        print("Skema sorting tidak valid!")

# Print riwayat pembelian suatu user
def riwayat(data, role):
    if role != "user":
        return
    user = data[4][0]
    # Filter game yang telah dibeli
    r = data[2][1:]
    temp = data[2][0]
    l = [temp[0:3]+temp[4:5]]
    for i in r:
        if i[3] == user:
            l += [i[0:3]+i[4:5]]
    print(essentials.rapikan_matriks(l))

# Mencari game di toko
def search_game_store(data, role):
    if role != "admin" and role != "user":
        return
    
    index = input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun = input("Masukkan Tahun Rilis Game: ")

    search_data = [index, nama, kategori, tahun, harga]
    data_game = data[1]
    game_found = [data_game[0]]
    
    for d in data_game:
        for i in range(5):
            if not (search_data[i] == "" or search_data[i] == d[i]):
                break
        else:
            game_found += [d]

    if essentials.banyak(game_found) > 1:
        print("Daftar game pada toko yang memenuhi kriteria:")
        print(essentials.rapikan_matriks(game_found))
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria")

# Mencari game yang dimiliki
def search_my_game(data, role):
    if role!='user':
      return
    
    index = input('Masukkan ID Game: ')
    year = input('Masukkan Tahun Rilis Game: ')

    game = data[3]
    game_arr = []
    
    # FILTER GAME
    for i in game:
        if i[1] == data[4][0]:
            # FIND CORRESPONDING GAME
            for j in data[1]:
                if j[0] == i[0]:
                    game_arr += [j[0:5]]
                    break

    if not game_arr:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        return

    found_game = []

    # FILTER INDEX
    for i in game_arr:
        if not(index == "" or index == i[0]):
            break
        if not(year == "" or year == i[3]):
            break
        found_game += [i]

    if found_game:
        found_game = [data[1][0][0:5]] + found_game
        print(essentials.rapikan_matriks(found_game))
    else:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

# Fungsi untuk membeli game
def buy_game(data, role):
    if role != "user":
        return
    user = data[4][0]

    index = input("Masukkan ID Game: ")
    game = ""
    for i in range(essentials.banyak(data[1])):
        if data[1][i][0] == index:
            game = i
            break
        
    if not game:
        print(f"Game dengan ID {index} tidak ditemukan!")
        return
    game_info = data[1][game]

    if int(game_info[5]) <= 0:
        print("Stok Game tersebut sedang habis!")
        return
    
    for i in data[3]:
        if i[0] == game_info[0] and i[1] == user:
            print("Anda sudah memiliki Game tersebut!")
            return

    if int(data[4][5]) < int(game_info[4]):
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        return
    
    # Masukkan ke riwayat
    data[2] += [[game_info[0], game_info[1], game_info[4], user, "2022"]]
    data[3] += [[game_info[0], user]]
    for i in range(essentials.banyak(data[0])):
        if data[0][i][0] == user:
            data[0][i][5] = str(int(data[0][i][5]) - int(game_info[4]))
    # Modifikasi stok
    data[1][game][5] = str(int(game_info[5]) - 1)

    print(f'Game "{game_info[1]}" berhasil dibeli!')
    
    return data

# Fungsi untuk melihat game yang dimiliki
def list_game(data, role):
    if role != "user":
        return

    user = data[4][0]
    # Filter owned
    owned = []
    for i in data[3]:
        if i[1] == user:
            owned += [i[0]]
    # Assign owned with game
    disp = []
    for i in data[1]:
        if i[0] in owned:
            disp += [i[:-1]]
    # Display game
    if not disp:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
        return
    disp = [data[1][0][:-1]] + disp
    print("Daftar game:")
    print(essentials.rapikan_matriks(disp))
    return
