from essentials import banyak
# Memvalidasi game
def validasi(game):
    try:
        for i in game[3:6]:
            int(i)
        return True
    except:
        return False

# Menambah game
def tambah_game(data, role):
    questions = ["nama game", "kategori", "tahun rilis", "harga", "stok awal"]

    if role != "admin":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        return
    
    index = int(data[1][-1][0][4:7]) + 1
    index = f'GAME{index:0>3}'
    temp = game = [index]
    while True:
        for i in questions:
            game = game + [input(f"Masukkan {i}: ")]
        if "" in game or not validasi(game):
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            game = temp
        else:
            break
    data[1] = data[1] + [game]
    print(f"Selamat! Berhasil menambahkan game {game[1]}.")
    return data

# Mengubah informasi game
def ubah_game(data, role):
    questions = ["nama game", "kategori", "tahun rilis", "harga", "stok awal"]
    
    if role != "admin":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        return
    
    index = input("Masukkan ID Game: ")
    for i in range(banyak(data[1])):
        if data[1][i][0] == index:
            mark = i
            break
    else:
        print("ID tidak ditemukan!")
        return
    for i in range(banyak(questions)):
        temp = input(f"Masukkan {questions[i]}: ")
        if temp != "":
            data[1][mark][i+1] = temp
    return data

# Mengubah stok
def ubah_stok(data, role):
    
    if role != "admin":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        return
    
    index = input("Masukkan ID Game: ")
    for i in range(banyak(data[1])):
        if data[1][i][0] == index:
            mark = i
            break
    else:
        print("Tidak ada game dengan ID tersebut!")
        return
    temp = int(input("Masukkan jumlah: "))
    cur = int(data[1][mark][5]) + temp
    if cur >= 0:
        data[1][mark][5] = str(cur)
    else:
        print(f"Stok game {data[1][mark][1]} gagal dikurangi karena stok kurang. Stok sekarang: {data[1][mark][5]} (< {abs(temp)})")
        return
    if temp >= 0:
        print(f"Stok game {data[1][mark][1]} berhasil ditambahkan. Stok sekarang: {cur}")
    else:
        print(f"Stok game {data[1][mark][1]} berhasil dikurangi. Stok sekarang: {cur}")
    return data

# Top-up certain user as admin
def top_up(data, role):
    
    if role != "admin":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        return

    u_name = input("Masukkan username: ")
    try:
        saldo = int(input("Masukkan saldo: "))
    except:
        print("Masukan tidak valid")
        return
    for i in range(banyak(data[0])):
        if data[0][i][1] == u_name:
            if int(data[0][i][5]) + saldo < 0:
                print("Masukan tidak valid")
                return
            data[0][i][5] = str(int(data[0][i][5]) + saldo)
            if saldo < 0:
                arg = "berkurang"
            else:
                arg = "bertambah"
            print(f"Top up berhasil. Saldo {data[0][i][2]} {arg} menjadi {data[0][i][5]}.")
            return data
    print(f'Username "{u_name}" tidak ditemukan')
    return
