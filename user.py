from essentials import banyak
from essentials import contain
import cipher
key = 8

allowed = list(chr(i) for i in range(ord('a'), ord('z')+1))+ list(chr(i) for i in range(ord('A'), ord('Z')+1))+['_', '-'] + list(str(i) for i in range(0, 10))

# Login (user as matrix containing user.csv)
def login(data, role):
    # Input user dan password
    user = input("Masukkan username: ")
    passw = input("Masukkan password: ")

    # Mengecek apakah user dan password benar
    for i in data[0]:
        if i[1] == user:
            if cipher.decipher(i[3], key) == passw:
                print(f"Halo {i[2]}! Selamat datang di “Binomo”.")
                data[4] = i
                return data
            else:
                print("Password salah!")
                return
    print("Username salah!")
    return

# Register (user as matrix containing user.csv)
def register(data, role):
    # Mengecek role
    if role != "admin":
        return

    # Input registrasi user
    name = input("Masukan nama: ")
    u_name = input("Masukkan username: ")
    passw = cipher.cipher(input("Masukkan password: "), key)

    # Mengecek apakah username sudah terpakai
    for i in data[0]:
        if i[1] == u_name:
            print(f"Username {u_name} sudah terpakai, silakan menggunakan username lain.")
            return

    # Mengecek apakah ada karakter yang tidak diizinkan di username
    allow = []
    for char in u_name:
        allow += [contain(allowed, char)]
    
    if contain(allow, False):
        print("Username mengandung karakter yang tidak diizinkan")
        return
    if contain(passw, ";"):
        print("Password mengandung karakter yang tidak diizinkan")
        return

    # Proses registrasi di database
    data[0] += [[str(banyak(data[0])), u_name, name, passw, "user", "0"]]
    print(f'Username {u_name} telah berhasil register ke dalam "Binomo"')
    
    return data
