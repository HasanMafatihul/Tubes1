#akses:Admin

def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x

def register(role, user_arr):
   if role!='admin':
      return
   #memastikan username   
   s=False
   x=" !@#$%^&*()+=|\{[}]:;~`'<>?/" or '"' 
   nama = input('Masukan nama: ')
   uName = input('Masukan username: ')
   while not s:
      if any(c in x for c in uName):
         uName = input('Masukan username: ')
         s=True
   password = input('Masukan password: ')
      
   
   #membaca dari file user.csv
   for i in range(banyak(user_arr)):
      if (uName==user_arr[i][1]):
         print('\nUsername',uName,'sudah terpakai, silakan menggunakan username lain.')
         break
      else:
         print('\nUsername',uName,'telah berhasil register ke dalam "Binomo".')
         break



r# egister('admin', [['001', 'Etawa8403', 'Hanif', 'adadeh', 'Admin', ' '], ['002', 'JackAss_02', 'Andro', 'tehsosro', 'Admin', ' '], ['003', 'Dika-03', 'Andika', 'parkua', 'user', ' ']] )  


