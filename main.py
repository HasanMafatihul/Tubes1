import argparse
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
import os
import sys
import system
import essentials
import user
import normal
import admin
from tic_tac_toe import tic_tac_toe
from magic_conch import magic

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


print('Selamat datang di antarmuka "Binomo"')

# Deklarasi command
cmd = [["help", system.help], ["q", system.quit], ["exit", system.quit], ["save", system.save_folder],
       ["login", user.login], ["register", user.register],
       ["tambah_game", admin.tambah_game], ["ubah_game", admin.ubah_game], ["ubah_stok", admin.ubah_stok], ["topup", admin.top_up],
       ["list_game_toko", normal.listing], ["riwayat", normal.riwayat], ["search_game_at_store", normal.search_game_store],
       ["search_my_game", normal.search_my_game], ["buy_game", normal.buy_game], ["list_game", normal.list_game],
       ["tic_tac_toe", tic_tac_toe], ["magic_conch", magic]]

system.help(data, "guest")

# Sebelum login
while True:
    i = input(">>> ")
    do = essentials.switch(i, cmd)
    if not do:
        continue
    r = do(data, "guest")
    if r: data = r
    if data[4] != []:
        break

system.help(data, data[4][4])

# Program UI utama
while True:
    i = input(">>> ")
    do = essentials.switch(i, cmd)
    if not do:
        continue
    if data[4] == []:
        r = do(data, "guest")
        if r: data = r
    else:
        r = do(data, data[4][4])
        if r: data = r
    
