def search_game_inventory(data_inventory,banyak_game_inventory):

    id = input("Masukkan ID Game: ")
    tahun = input("Masukkan Tahun Rilis Game: ")

    index = 0
    tidak_ketemu = True
    while tidak_ketemu:
        if data_inventory[index][1] == id and data_inventory[index][5] == tahun:
            tidak_ketemu = False
        else:
            index += 1
            if index == banyak_game_inventory:
                tidak_ketemu = False

    print("Daftar game pada inventory yang memenuhi kriteria:")
    if index < banyak_game_inventory:
        for j in range(7):
            print(data_inventory[index][j], "|", end="")
    else:
        print("Tidak ada game pada inventory yang memenuhi kriteria")