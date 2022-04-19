import essentials

scheme = ["tahun", "harga", ""]

# Mengeluarkan listing game berdasarkan skema sorting tertentu
def listing(data, role):
    l = data[1][1:]
    skema = input("Skema sorting : ")
    if skema[:-1] in scheme:
        if skema[:-1] == "tahun":
            kolom = 3
            z = skema[-1]
        elif skema[:-1] == "harga":
            kolom = 4
            z = skema[-1]
        else:
            kolom = 0
            z = "+"
        list_index = [0] + essentials.urutan(l, kolom, z)
        
        # Filter menggunakan index
        list_filtered = []
        for i in list_index:
            list_filtered += [data[1][i]]
        print(essentials.rapikan_matriks(list_filtered))
    else:
        print("Skema sorting tidak valid!")

# Print riwayat pembelian suatu user
def riwayat(data, role):
    if role != "user":
        return
    user = data[4][0]
    # Filter game yang telah dibeli
    r = data[2][1:]
    temp = data[2][0]
    l = [temp[0:3]+temp[4:5]]
    for i in r:
        if i[3] == user:
            l += [i[0:3]+i[4:5]]
    print(essentials.rapikan_matriks(l))

