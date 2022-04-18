questions = ["nama game", "kategori", "tahun rilis", "harga"]

def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x 

# Menambah game
def ubah_game(role, game_arr):
    if role != "admin":
        return
    index = input("Masukkan ID Game: ")
    for i in range(banyak(game_arr)):
        if game_arr[i][0] == index:
            mark = i
            break
    else:
        print("ID tidak ditemukan!")
        return
    temp = ""
    for i in range(banyak(questions)):
        temp = input(f"Masukkan {questions[i]}: ")
        if temp != "":
            game_arr[mark][i+1] = temp
    return game_arr

print(ubah_game("admin", [["GAME001", "Halo", "Shooter", "2022", "100.000", "1"]]))
