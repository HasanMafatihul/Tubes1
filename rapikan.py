def banyak(l):
    c = 0
    for i in l:
        c += 1
    return c

def longest_arr(data: list, x):
    panjang_string = banyak(data[0][x])
    for i in range(banyak(data)):
        if panjang_string < banyak(data[i][x]):
            panjang_string = banyak(data[i][x])
    return panjang_string

def rapikan(data: list):
    o = ""
    l = []

    # Buat list string terpanjang di tiap kolom
    for i in range(banyak(data[0])):
        l = l + [longest_arr(data, i)]

    
    for i in range(banyak(data)):
        for j in range(banyak(data[i])):
            o += f"{data[i][j]: <{l[j]}} |"
        o += "\n"
    return o
