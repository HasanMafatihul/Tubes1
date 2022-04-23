def cek_menang(data):
    # horizontal
    for i in range(3):
        if data[i][0] == data[i][1] == data[i][2] == ("X" or "Y"):
            return data[i][1]
    # vertikal
    for j in range(3):
        if data[0][j] == data[1][j] == data[2][j] == ("X" or "Y"):
            return data[1][j]
    # diagonal
    if (data[0][0] == data[1][1] == data[2][2] == ("X" or "Y")) or (data[0][2] == data[1][1] == data[2][0] == ("X" or "Y")):
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
    if x >= 3 or y >= 3:
        return False
    else:
        if data[x][y] != "#":
            return False
def print_papan(papan):
    print("Status Papan")
    for i in range(3):
        for j in range(3):
            print(papan[i][j], end="")
        print("")

def tic_tac_toe(data, role):
    # WELCOME
    print(f'{"Permainan Tic Tac Toe":-^41}')
    
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
        X = int(input("X: "))
        Y = int(input("Y: "))
        while input_valid(papan,X,Y) == False:
            print("Kotak tidak valid.")
            X = int(input("X: "))
            Y = int(input("Y: "))
        papan[X][Y] = pemain 
        print_papan(papan)
        if cek_seri(papan) == True:
            menang = "seri"
        else:
            menang = cek_menang(papan)

    if menang == "seri":
        print("Permainan seri") 
    else:
        print(f'Pemain "{menang}" menang')
