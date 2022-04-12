import os
cd = input("Masukkan nama folder penyimpanan: ")
print("Saving...")
ada_game = False
ada_riwayat = False
ada_user = False


if not os.path.exists(str(cd)):
    os.makedirs(str(cd))

for files in os.walk(cd):
    if files == "game.csv":
        ada_game = True
    if files == "riwayat.csv":
        ada_riwayat = True
    if files == "user.csv":
        ada_user = True

if ada_game == True:
    data_game = open(f"{cd}/game.csv", "a")
    for i in data_game:
        data_game.writelines([f"{i}"])
    data_game.close()

if ada_game == False:
    data_game = open(f"{cd}/game.csv", "w")
    for i in data_game:
        data_game.writelines([f"{i}"])
    data_game.close()

if ada_riwayat == True:
    data_riwayat = open(f"{cd}/riwayat.csv", "a")
    for i in data_riwayat:
        data_riwayat.writelines([f"{i}"])
    data_riwayat.close()

if ada_riwayat == False:
    data_riwayat = open(f"{cd}/riwayat.csv", "w")
    for i in data_riwayat:
        data_riwayat.writelines([f"{i}"])
    data_riwayat.close()

if ada_user == True:
    data_user = open(f"{cd}/user.csv", "a")
    for i in data_user:
        data_user.writelines([f"{i}"])
    data_user.close()

if ada_user == True:
    data_user = open(f"{cd}/user.csv", "w")
    for i in data_user:
        data_user.writelines([f"{i}"])
    data_user.close()

