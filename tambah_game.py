questions = ["nama game", "kategori", "tahun rilis", "harga", "stok awal"]

def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x 

# Menambah game
def tambah_game(role, game_arr):
    if role != "admin":
        return
    index = int(game_arr[banyak(game_arr)-1][0][4:7]) + 1
    index = f'GAME{index:0>3}'
    temp = game = [index]
    while True:
        for i in questions:
            game = game + [input(f"Masukkan {i}: ")]
        if "" in temp:
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            game = temp
        else:
            break
    game_arr = game_arr + game
    print(f"Selamat! Berhasil menambahkan game {game[1]}.")
    return game_arr
