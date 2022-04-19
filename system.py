import essentials
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
        data1 = data1 + [text[:-1]]
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
def save_folder(data, role):
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
            y = y[:-1] + "\n"
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
def help(data: list, role: str):
    print(f"{'HELP':-^20}")

# Menutup program
def quit(data, role):
    while True:
        i = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if i.lower() == "y":
            save_folder(data, role)
            break
        elif i.lower() == "n":
            break
    exit()
