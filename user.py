allowed = list(chr(i) for i in range(ord('a'), ord('z')+1))+ list(chr(i) for i in range(ord('A'), ord('Z')+1))+['_', '-'] + list(str(i) for i in range(0, 10))

def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x 

# Login (user as matrix containing user.csv) -> return user_data
def login(user_arr):
    user = input("Masukkan username: ")
    passw = input("Masukkan password: ")
    for i in user_arr:
        if i[1] == user:
            if i[3] == passw:
                print(i[2])
                return i
            else:
                break
    return None

# Register (user as matrix containing user.csv) -> return modified user array
def register(user_arr, role):
    if role != "admin":
        return None
    name = input("Masukan nama: ")
    u_name = input("Masukkan username: ")
    passw = input("Masukkan password: ")
    for i in user_arr:
        if i[1] == u_name:
            print(f"Username {u_name} sudah terpakai, silakan menggunakan username lain.")
            return None
    allow = [char in allowed for char in u_name]
    if False in allow:
        print("Username mengandung karakter yang tidak diizinkan")
        return None
    user_arr += [[user_arr[banyak(user_arr) - 1][0] + 1, u_name, name, passw, "user", 0]]
    print(f'Username {u_name} telah berhasil register ke dalam "Binomo"')
    return user_arr

print(register([[0, "hasan"]], "admin"))
