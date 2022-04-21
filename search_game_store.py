def search_game_store(data_game,banyak_game):

    id = input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun = input("Masukkan Tahun Rilis Game: ")

    index = 0
    tidak_ketemu = True
    while tidak_ketemu:
        if data_game[index][1] == id and data_game[index][2] == nama and data_game[index][3] == harga and \
                data_game[index][4] == kategori and data_game[index][1] == tahun:
            tidak_ketemu = False
        else:
            index += 1
            if index == banyak_game:
                tidak_ketemu = False

    print("Daftar game pada toko yang memenuhi kriteria:")
    if index < banyak_game:
        for j in range(7):
            print(data_game[index][j], "|", end="")
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria")