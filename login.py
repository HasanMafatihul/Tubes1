# Login (user as matrix containing user.csv)
def login(user_arr):
    user = input("Masukkan username\t: ")
    passw = input("Masukkan password\t: ")
    for i in user_arr:
        if i[1] == user:
            if i[3] == passw:
                print(i[2])
                return i
            else:
                break
    return None
