import os
def cek_menang(data):
    # horizontal
    for i in range(3):
        if data[i][0] == data[i][1] == data[i][2] == "X" or data[i][0] == data[i][1] == data[i][2] == "O":
            return data[i][1]
    # vertikal
    for j in range(3):
        if data[0][j] == data[1][j] == data[2][j] == "X" or data[0][j] == data[1][j] == data[2][j] == "O":
            return data[1][j]
    # diagonal
    if (data[0][0] == data[1][1] == data[2][2] == "X" or data[0][0] == data[1][1] == data[2][2] == "O") or (data[0][2] == data[1][1] == data[2][0] == "X" or data[0][2] == data[1][1] == data[2][0] == "X"):
        return data[1][1]
    else:
        return "-"
def cek_seri(data):
    seri = True
    for i in range(3):
        for j in range(3):
            if data[i][j] == "#":
                seri = False
    return seri
def input_valid(data,x,y):
    if x == "" or y == "":
        return False
    else:
        if int(x) > 3 or int(y) > 3 or int(x) < 1 or int(y) < 1:
            return False
        else:
            if data[int(x)-1][int(y)-1] != "#":
                return False
def print_papan(papan):
    print("Status Papan")
    for i in range(3):
        for j in range(3):
            print(papan[i][j], end="")
        print("")
def tic_tac_toe():
    # WELCOME
    print("================= Permainan Tic Tac Toe =================")
    print("Legenda: \n X : Pemain 1 \n O : Pemain 2")
    
    papan = [["#" for i in range(3)] for j in range(3)]

    print_papan(papan)

    giliran = 1
    menang = "-"
    while menang == "-":
        if giliran % 2 == 1:
            pemain = "X"
        else:
            pemain = "O"
        print(f'Giliran Pemain "{pemain}"')
        giliran += 1
        baris = input("baris: ")
        kolom = input("kolom: ")
        while input_valid(papan,baris,kolom) == False:
            print("Kotak tidak valid.")
            baris = input("baris: ")
            kolom = input("kolom: ")
        papan[int(baris)-1][int(kolom)-1] = pemain 
        os.system("cls")
        print_papan(papan)
        if cek_seri(papan) == True:
            menang = "seri"
        else:
            menang = cek_menang(papan)

    if menang == "seri":
        print("Permainan seri") 
    else:
        print(f'Pemain "{menang}" menang')
