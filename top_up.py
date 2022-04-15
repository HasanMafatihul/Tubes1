allowed = list(chr(i) for i in range(ord('a'), ord('z')+1))+ list(chr(i) for i in range(ord('A'), ord('Z')+1))+['_', '-'] + list(str(i) for i in range(0, 10))

def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x 

# Top-up certain user as admin
def top_up(role, user_arr):
    if role != "admin":
        return
    u_name = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo: "))
    if saldo <= 0:
        print("Masukan tidak valid")
        return user_arr
    for i in banyak(user_arr):
        if user_arr[i][1] == u_name:
            print(f"Top up berhasil. Saldo {user_arr[i][2]} bertambah menjadi 15000.")
            user_arr[i][5] += saldo
            return user_arr
    print(f'Username "{u_name}" tidak ditemukan')
    return user_arr
