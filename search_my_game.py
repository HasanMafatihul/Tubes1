def banyak(li):
    x = 0
    for i in li:
        x += 1
    return x

# Mencari game
def search_my_game(role, game_arr):
   if role!='user':
      return
   index1=input('Masukkan ID Game: ')
   index2=input('Masukkan Tahun Rilis Game: ')
   how=''
   y=0
   for i in range (banyak(game_arr)):
      if game_arr[i][1]==index1 and game_arr[i][5]==index2:
         how='found'
         y+=1
         print(y,'|',game_arr[i][1],'|',game_arr[i][2],'|',game_arr[i][3],'|',game_arr[i][4],'|',game_arr[i][5])
         break
      elif game_arr[i][1]==index1:
         how='found'
         y+=1
         print(y,'|',game_arr[i][1],'|',game_arr[i][2],'|',game_arr[i][3],'|',game_arr[i][4],'|',game_arr[i][5])
         break
      elif  game_arr[i][5]==index2:
         how='found'
         y+=1
         print(y,'|',game_arr[i][1],'|',game_arr[i][2],'|',game_arr[i][3],'|',game_arr[i][4],'|',game_arr[i][5])
         continue

   if not how=='found' :
      print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
         
         
            

search_my_game('user', [['1', 'GAME001', 'Elden Ring', '599000', 'Adventure, Action, Open World', '2022'], ['2', 'GAME002', 'Dark Souls 1: Remastered', '420000', 'Adventure, Action', '2018'], ['3', 'GAME003', 'Dark Souls 2', '460000', 'Adventure, Action', '2014'], ['4', 'GAME004', 'Dark Souls 3', '587000', 'Adventure, Action', '2016'], ['5', 'GAME005', 'God of War', '729000', 'Adventure, Action', '2018'], ['6', 'GAME006', 'The Last of Us', '525000', 'Adventure, Action, Open World', '2013'], ['7', 'GAME007', 'The Last of Us 2', '650000', 'Adventure, Action, Open World', '2020'], ['8', 'GAME008', "Assassin's Creed Valhalla", '600000', 'Adventure, Action, Open World', '2020'], ['9', 'GAME009', 'DOOM Eternal', '329999', 'Adventure, Action', '2020'], ['10', 'GAME010', 'Far Cry 6', '620000', 'Adventure, Action, Open World', '2021'], ['11', 'GAME011', 'Horizon Zero Dawn', '364500', 'Adventure, Action, Open World', '2017']])