import essentials
from essentials import slice_str
import os

# Membuka file csv di suatu lokasi (cd)
def load_csv(cd):
    # membuka file csv
    with open (cd) as x:
        lines = x.readlines()
    
    # parsing data
    data = []
    for i in range(essentials.banyak(lines)):
        text = ""
        data1 = []
        for j in lines[i]:
            if j != ";":
                text += j
            else:
                data1 = data1 + [text]
                text = ""
        data1 = data1 + [slice_str(text,0,-1)]
        data = data + [data1]
    
    return data

# Membuka file-file yang dibutuhkan dari suatu folder
# Output: [user, game, riwayat, kepemilikan]
# Asumsi file bisa dibuka
def load_folder(cd):
    o = []
    e = ["user", "game", "riwayat", "kepemilikan"]
    # Membuka setiap folder sesuai daftar e
    for i in e:
        o = o + [load_csv(cd + "\\" + i + ".csv")]
    return o

# Menyimpan semua file dalam satu folder
def save_folder(data):
    # Meminta lokasi penyimpanan
    cd = input("Masukkan nama folder penyimpanan: ")
    print("Saving...")
    # De-parsing data
    o = []
    for d in data:
        x = ""
        for i in d:
            y = ""
            for j in i:
                y += j + ";"
            y = slice_str(y,0,-1) + "\n"
            x += y
        o = o + [x]
    data = o
    
    # Daftar file-file yang disimpan
    e = ["user", "game", "riwayat", "kepemilikan"]

    # Jika folder tidak ada, buat folder
    if not os.path.exists(str(cd)):
        os.makedirs(str(cd))
    
    for f in range(essentials.banyak(e)):
        data_game = open(f"{cd}/" + e[f] + ".csv", "w")
        data_game.writelines(data[f])
        data_game.close()

    print(f"Data telah disimpan pada folder {cd}!")

# Membuka menu help
def help(role: str):
    if role == "admin":
        print('''
        ======================== HELP ========================
        -> register - Untuk melakukan registrasi user baru
        -> login - Untuk melakukan login ke dalam sistem
        -> tambah_game - Untuk menambah game yang dijual pada toko
        -> ubah_game - Untuk mengubah informasi game yang dijual pada toko
        -> ubah_stok - Untuk mengubah banyak stok game yang dijual
        -> list_game_toko - Untuk melihat list game yang dijual pada toko
        -> search_game_at_store - Untuk mencari game di toko
        -> topup - Untuk menambah saldo pada User
        -> magic_conch - Untuk bermain Magic Conch Shell
        -> tic_tac_toe - Untuk bermain Tic Tac Toe
        -> help - Untuk memberikan panduan penggunaan sistem
        -> save - Untuk melakukan penyimpanan ke dalam file
        -> exit - Untuk keluar dari aplikasi
        ''')
    elif role == "user":
        print('''
        ======================== HELP ========================
        -> login - Untuk melakukan login ke dalam sistem
        -> list_game_toko - Untuk melihat list game yang dijual pada toko
        -> buy_game - Untuk membeli game di toko
        -> list_game - Untuk melihat list game yang dimiliki
        -> search_my_game - Untuk mencari game yang dimiliki
        -> search_game_at_store - Untuk mencari game di toko
        -> riwayat - Untuk melihat list riwayat pembelian game
        -> magic_conch - Untuk bermain Magic Conch Shell
        -> tic_tac_toe - Untuk bermain Tic Tac Toe
        -> help - Untuk memberikan panduan penggunaan sistem
        -> save - Untuk melakukan penyimpanan ke dalam file
        -> exit - Untuk keluar dari aplikasi
        ''')
    else:
        print('''
        ======================== HELP ========================
        -> login - Untuk melakukan login ke dalam sistem
        -> magic_conch - Untuk bermain Magic Conch Shell
        -> tic_tac_toe - Untuk bermain Tic Tac Toe
        -> help - Untuk memberikan panduan penggunaan sistem
        -> save - Untuk melakukan penyimpanan ke dalam file
        -> exit - Untuk keluar dari aplikasi
        ''')

# Menutup program
def quit(data):
    while True:
        i = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if i.lower() == "y":
            save_folder(data)
            break
        elif i.lower() == "n":
            break
    os.system("cls")
    print("Terima kasih telah menggunakan program Binomo")
    exit()
