import argparse
from msilib.schema import Error
import os
import system
import essentials
import user
import normal
import admin
from tic_tac_toe import tic_tac_toe
from magic_conch import magic
import time

parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs='?', const='')
args = parser.parse_args()
cd = args.folder

# Mengecek keberadaan folder
if cd:
    if not os.path.exists(str(cd)):
        print(f'Folder "{cd}" tidak ditemukan.')
        exit()
else:
    print("Tidak ada nama folder yang diberikan!")
    exit()

try:
    f = open(cd + "\\game.csv")
    f = open(cd + "\\user.csv")
    f = open(cd + "\\riwayat.csv")
    f = open(cd + "\\kepemilikan.csv")
    f.close()
except:
    print("Folder tidak mengandung file yang diperlukan!")
    exit()

print("Loading...")

# Deklarasi data
data = system.load_folder(cd)
data = data + [[]]
# Struktur data (user, game, riwayat, kepemilikan, data user saat ini)

# Deklarasi command
cmd = [["help", system.help], ["q", system.quit], ["exit", system.quit], ["save", system.save_folder],
       ["login", user.login], ["register", user.register],
       ["tambah_game", admin.tambah_game], ["ubah_game", admin.ubah_game], ["ubah_stok", admin.ubah_stok], ["topup", admin.top_up],
       ["list_game_toko", normal.listing], ["riwayat", normal.riwayat], ["search_game_at_store", normal.search_game_store],
       ["search_my_game", normal.search_my_game], ["buy_game", normal.buy_game], ["list_game", normal.list_game],
       ["tic_tac_toe", tic_tac_toe], ["magic_conch", magic]]

# Sebelum login
selesai = False
while selesai == False:
    time.sleep(1)
    print("Selamat datang di antarmuka Program Toko Game K10-08")
    time.sleep(1)
    essentials.print_perintah("")
    command = input("Masukkan perintah : ")
    os.system('cls')
    do = essentials.switch(command, cmd)
    if command == "login":
        r = do(data)
        if data[4] != []:
            break
    elif command == "help":
        r = do("guest")
    elif command == "exit":
        r = do(data)
    elif command == "tic_tac_toe" or command == "magic_conch":
        r = do()  
    else:
        if not do:
            print("Masukkan tidak valid, silahkan coba lagi")
            time.sleep(1)
            continue
        try:
            r = do(data, "guest")
            if data[4] != []:
                break
        except:
            Error
            print("Masukkan tidak valid, silahkan coba lagi")
    input("Tekan ENTER untuk keluar")
    os.system('cls')

# Program UI utama
selesai = False
while selesai == False:
    time.sleep(1)
    essentials.print_perintah(data[4][4])
    command = input("Masukkan perintah : ")
    os.system('cls')
    do = essentials.switch(command, cmd)
    if command == "save" or command == "exit" or command == "list_game_toko":
        r = do(data)
    elif command == "help":
        r = do(data[4][4])
    elif command == "tic_tac_toe" or command == "magic_conch":
        r = do()
    else:
        if not do:
            print("Masukkan tidak valid, silahkan coba lagi")
            time.sleep(1)
            continue
        try:
            r = do(data, "guest")
            if data[4] != []:
                break
        except:
            Error
            print("Masukkan tidak valid, silahkan coba lagi")
        else:
            r = do(data, data[4][4])
    input("Tekan ENTER untuk keluar")
    os.system('cls')
