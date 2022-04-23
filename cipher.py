from essentials import slice_str

def length(x):
    c = 0
    for i in x:
        c += 1
    return c

def cipher(txt, key):
    txt = str(txt)
    size = length(txt)
    # Shifting character
    temp = bytearray(txt, "utf-8")
    for i in range(length(temp)):
        temp[i] = temp[i] + key
    c = temp.decode("ascii")
    # Salt
    t = key % size
    c = slice_str(c, 0, t) + c + slice_str(c, t, size)
    return c

def decipher(txt, key):
    size = int(length(txt)/2)
    # Remove salt
    t = key % size
    txt = slice_str(txt, 0, t) + slice_str(txt, t+size, length(txt))
    # Shift character
    temp = bytearray(txt, "ascii")
    for i in range(length(temp)):
        temp[i] = temp[i] - key
        
    c = temp.decode("utf-8")
    return c
