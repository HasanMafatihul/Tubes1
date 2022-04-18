def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x 

# Menambah game
def ubah_stok(role, game_arr):
    if role != "admin":
        return
    index = input("Masukkan ID Game: ")
    for i in range(banyak(game_arr)):
        if game_arr[i][0] == index:
            mark = i
            break
    else:
        print("Tidak ada game dengan ID tersebut!")
        return
    temp = int(input("Masukkan jumlah: "))
    cur = int(game_arr[mark][5]) + temp
    if cur >= 0:
        game_arr[mark][5] = str(cur)
    else:
        print(f"Stok game {game_arr[mark][1]} gagal dikurangi karena stok kurang. Stok sekarang: {game_arr[mark][5]} (< {abs(temp)})")
        return
    if temp >= 0:
        print(f"Stok game {game_arr[mark][1]} berhasil ditambahkan. Stok sekarang: {cur}")
    else:
        print(f"Stok game {game_arr[mark][1]} berhasil dikurangi. Stok sekarang: {cur}")
    return game_arr

#print(ubah_stok("admin", [["GAME001", "Halo", "Shooter", "2022", "100.000", "1"]]))
