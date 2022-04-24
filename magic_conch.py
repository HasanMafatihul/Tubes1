import time

def magic():
    input("Apa pertanyaanmu? ")
    # dapatkan nilai detik dari jam sekarang
    y = time.gmtime().tm_sec

    # olah nilai detik tersebut menjadi random number
    x = (3*(y) + 10) % 69
    time.sleep(1)
    if x < 5:
        print("Ya")
    elif x >= 5 and x < 10:
        print("Tidak")
    elif x >= 10 and x < 15:
        print("Mungkin")
    elif x >= 15 and x < 20:
        print("Tidak mungkin")
    elif x >= 20 and x < 25:
        print("WANGYYYYYYYYY")
    elif x >= 25 and x < 30:
        print("STONKS")
    elif x >= 30 and x < 35:
        print("lah mendingan gacha...")
    elif x >= 35 and x < 40:
        print("¿Quieres?")
    elif x >= 40 and x < 45:
        print("a mimir")
    elif x >= 45 and x < 50:
        print("Jauh-jauh beli game tapi malah main magic conch")
    elif x >= 50 and x < 55:
        print("Jangan nanya terus deh, conch capek")
    else:
        print("Mending kerjain laprak daripada nanya conch terus")