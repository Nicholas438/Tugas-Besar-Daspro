# Fungsi fungsi general
def count_row(file):
    # Subprogram untuk menghitung jumlah baris dari file csv
    
    # Kamus Lokal
    # rowcount: int

    # Algoritma
    # Inisialisasi rowcount menjadi 0
    rowcount  = 0
    # Iterasi menghitung count sepanjang file
    for row in file:
        rowcount+= 1
    return rowcount

def length(sentence):
    # Menghitung panjang dari suatu string

    # Kamus Lokal
    # len : int
    # sentence: string

    # Algoritma
    len = 0
    for i in sentence:
        len+=1
    return len

def valid_input(number,type1,type2):
    # Melakukan pengulangan sehingga input adalah integer dan mengembalikan pesan error
    while not cek_int(number):
        print(type1,"harus bilangan bulat.")        # Mengembalikan pesan error
        number = input("Masukkan "+type2+": ")      # Melakukan pengulangan input

# Fungsi khusus
# Untuk F02. Register
def validitas_username(username):
    # Melihat jika username sesuai kriteria

    # Kamus Lokal
    # username_valid : Bool
    # i: int

    # Algoritma
    username_valid = True               # Inisialisasi validitas sebagai True
    for i in range(length(username)):   # Iteritas sepanjang length username
        if ord(username[i])<45 or 45<ord(username[i])<48 or 57<ord(username[i])<65 or 90<ord(username[i])<95 or ord(username[i])==96 or ord(username[i])>122:
            username_valid = False      # Jika ditemukan karakter tidak sesuai maka dikembalikan false
            break
    return username_valid

# Untuk topup dan tic tac toe
def cek_int(number):
    # Mengecek jika suatu inputan adalah integer

    # Kamus Lokal
    # i: int

    # Algoritma
    for i in range(length(number)):
        if not(48<=ord(number[i])<=57):
            return False                # Jika salah satu karakter bukanlah nomor maka akan direturn False
    return True

# Untuk F07. Listing Game
def sort_ascending(skema,obj,obj2,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort):
    # Mengsortir list dari kecil ke besar menggunakan selection sort

    # Kamus lokal
    # count_min,j,i: int
    # obj,obj2: array of string
    # nama_game_sort,id_game_sort,kategori_game_sort,stok_sort: array of string
    global row_game

    # Algoritma
    for j in range(1,row_game):
        count_min = j                       # Penentuan elemen terkecil
        for i in range(j+1,row_game):
            if skema == "harga+":
                if int(obj[i])<int(obj[count_min]):
                    count_min = i 
            else:
                if obj[i]<obj[count_min]:
                    count_min = i 
        if count_min != j:                  # Mengubah elemen terkecil menjadi elemen ke-j jika elemen terkecil bukan elemen ke-j
            obj[j],obj[count_min] = obj[count_min],obj[j]
            nama_game_sort[j],nama_game_sort[count_min] = nama_game_sort[count_min],nama_game_sort[j]
            id_game_sort[j],id_game_sort[count_min] = id_game_sort[count_min],id_game_sort[j]
            obj2[j],obj2[count_min] = obj2[count_min],obj2[j]
            kategori_game_sort[j],kategori_game_sort[count_min] = kategori_game_sort[count_min],kategori_game_sort[j]
            stok_sort[j],stok_sort[count_min] = stok_sort[count_min],stok_sort[j]
    return obj,nama_game_sort,id_game_sort,obj2,kategori_game_sort,stok_sort 

def sort_descending(skema,obj,obj2,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort):
    # Mengurutkan list dari besar ke kecil menggunakan selection sort
    # Kamus Lokal
    # count_max,j,i: int
    # obj,obj2: array of string
    # nama_game_sort,id_game_sort,kategori_game_sort,stok_sort: array of string
    global row_game

    # Algoritma
    for j in range(1,row_game):
        count_max = j                       # Pencarian elemen maximum
        for i in range(j+1,row_game):
            if skema == "harga-":
                if int(obj[i])<int(obj[count_min]):
                    count_min = i 
            else:
                if obj[i]<obj[count_min]:
                    count_min = i 
        obj[j],obj[count_max] = obj[count_max],obj[j]               # Penukaran elemen
        nama_game_sort[j],nama_game_sort[count_max] = nama_game_sort[count_max],nama_game_sort[j]
        id_game_sort[j],id_game_sort[count_max] = id_game_sort[count_max],id_game_sort[j]
        obj2[j],obj2[count_max] = obj2[count_max],obj2[j]
        kategori_game_sort[j],kategori_game_sort[count_max] = kategori_game_sort[count_max],kategori_game_sort[j]
        stok_sort[j],stok_sort[count_max] = stok_sort[count_max],stok_sort[j]
    return obj,nama_game_sort,id_game_sort,obj2,kategori_game_sort,stok_sort   

def sorting(skema,tahun_rilis_sort,nama_game_sort,id_game_sort,harga_sort,kategori_game_sort,stok_sort):
    # Melakukan sorting sesuai dengan fungsi sort ascending dan descending
    
    # Kamus Lokal
    # skema: string
    # nama_game_sort,id_game_sort,kategori_game_sort,stok_sort: array of string
    global tahun_rilis,nama_game,id_game,harga,kategori_game,stok
    
    # Algoritma
    if skema == "tahun+":
        sort_ascending(skema,tahun_rilis_sort,harga_sort,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "tahun-":
        sort_descending(skema,tahun_rilis_sort,harga_sort,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "harga+":
        sort_ascending(skema,harga_sort,tahun_rilis_sort,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "harga-":
        sort_descending(skema,harga_sort,tahun_rilis_sort,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "":                       # Tersortir sesuai id game jika skema kosong
        sort_ascending(skema,id_game_sort,tahun_rilis_sort,nama_game_sort,harga_sort,kategori_game_sort,stok_sort)
    else:                                   # Pesan error skema tidak sesua
        return False

# Untuk F10. Mencari game yang dimiliki
def data_game(id_game_list,tahun_rilis_list,game_index):
    # Mendata game yang dimiliki sebagai user

    # Kamus Lokal
    # i,j: int
    # game_index: array of int
    # id_game_list,tahun_rilis_list : array of string
    global row_kepemilikan, id_game_kepemilikan, user_id_kepemilikan,id_game,tahun_rilis,id_user,login_count

    # Algoritma
    for i in range(row_kepemilikan):
        if user_id_kepemilikan[i] == id_user[login_count]:      # Mencari id user di data kepemilikan
            for j in range(row_game):
                if id_game_kepemilikan[i] == id_game[j]:        # Menambah game user ke dalam data temporary
                    id_game_list += [id_game[j]]
                    tahun_rilis_list += [tahun_rilis[j]]
                    game_index += [j]
    return id_game_list,tahun_rilis_list,game_index

# Untuk Bonus 3. Tic Tac Toe
def winning_condition(papan,pemain):
    # Melihat jika salah satu pemain sudah menang dalam tic tac toe
    # Menang diagonal
    
    # Kamus Lokal
    # papan: array of array of char
    # pemain: char
    # win: Bool
    # i: int

    win = False
    if papan[1][1] == pemain and ((papan[0][0] == pemain and papan[2][2] == pemain) or (papan[0][2] == pemain and papan [2][0]== pemain)):
        win = True
    # Menang horizontal
    for i in range(3):
        if papan[0][i] == pemain and papan[1][i] == pemain and papan[2][i] == pemain:
            win = True
    # Menang vertikal
    for i in range(3):
        if papan[i][0] == pemain and papan[i][1] == pemain and papan[i][2] == pemain:
            win = True
    return win


    

def print_papan(papan):
    # Memprint papan tic tac toe

    # Kamus Lokal
    # i,j: int
    # papan: array of array of char

    # Algoritma
    for i in range(3):
        for j in range(3):
            print(papan[j][i],end = "")
        print("")
