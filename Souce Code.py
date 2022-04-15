# Tubes Daspro


# Kamus

import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("datafolder",help = "Folder tempat data.csv")
args = parser.parse_args()
current_dir = os.getcwd()
data_path = os.path.join(current_dir,args.datafolder,"game.csv")




# Daftar fungsi dan prosedur
# Inisialisasi pengubah file csv menjadi list
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

def validitas_username(username):
    username_valid = True
    for i in range(length(username)):
        if ord(username[i])<45 or 45<ord(username[i])<48 or 57<ord(username[i])<65 or 90<ord(username[i])<95 or ord(username[i])==96 or ord(username[i])>122:
            username_valid = False
            break
    return username_valid

def cek_int(number):
    # Mengecek jika suatu inputan adalah integer
    for i in range(length(number)):
        if not(48<=ord(number[i])<=57):
            return False
    return True

def valid_input(number,type1,type2):
    while not cek_int(number):
        print(type1,"harus bilangan bulat.")
        number = input("Masukkan "+type2+": ")

# Inisialisasi mengubah semua csv menjadi list
def parsing_file1(file,id,var1,var2,var3,var4,var5):
    # Subprogram untuk menginisialisasi file user.csv dan game.csv
    global row_user,row_game
    with open(data_path,'r') as f:
        Lines = f.readlines()
    
    count = 0
    for line in Lines:
        id[count] = ""
        i = 0
        while i<length(line):
            if line[i] !=";":
                id[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var1[count] = ""
        while i<length(line):
            if line[i] !=";":
                var1[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var2[count] = ""
        while i<length(line):
            if line[i] !=";":
                var2[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var3[count] = ""
        while i<length(line):
            if line[i] !=";":
                var3[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var4[count] = ""
        while i<length(line):
            if line[i] !=";":
                var4[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var5[count] =  ""
        if count != (row_user-1) and count != (row_game-1):
            while i<(length(line)-1):
                if line[i] !=";":
                    var5[count]+=line[i]
                    i+=1
                else:
                    break
        elif count == (row_user-1) or count == (row_game-1):
            while i<(length(line)):
                if line[i] !=";":
                    var5[count]+=line[i]
                    i+=1
                else:
                    break
        count+=1
    return id,var1,var2,var3,var4,var5

def parsing_file2(id_game_riwayat,var1,var2,var3,var4):
    # Subprogram untuk menginisialisasi file riwayat.csv

    with open(data_path,'r') as f:
        Lines = f.readlines()
    
    count = 0
    for line in Lines:
        id_game_riwayat[count] = ""
        i = 0
        while i<length(line):
            if line[i] !=";":
                id_game_riwayat[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var1[count] = ""
        while i<length(line):
            if line[i] !=";":
                var1[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var2[count] = ""
        while i<length(line):
            if line[i] !=";":
                var2[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var3[count] = ""
        while i<length(line):
            if line[i] !=";":
                var3[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var4[count] = ""
        if count != (row_riwayat-1):
            while i<(length(line)-1):
                if line[i] !=";":
                    var4[count]+=line[i]
                    i+=1
                else:
                    break
        else:
            while i<length(line):
                if line[i] !=";":
                    var4[count]+=line[i]
                    i+=1
                else:
                    break            
        count+=1
    return id_game_riwayat,var1,var2,var3,var4

def parsing_file3(id_game_kepemilikan,var1):
    # Subprogram untuk menginisialisasi file riwayat.csv

    with open(data_path,'r') as f:
        Lines = f.readlines()
    
    count = 0
    for line in Lines:
        i = 0
        id_game_kepemilikan[count] = ""
        while i<length(line):
            if line[i] !=";":
                id_game_kepemilikan[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var1[count] = ""
        if count != (row_kepemilikan-1):
            while i<(length(line)-1):
                if line[i] !=";":
                    var1[count]+=line[i]
                    i+=1
                else:
                    break
        else:
            while i<(length(line)):
                if line[i] !=";":
                    var1[count]+=line[i]
                    i+=1
                else:
                    break
        count+=1
    return id_game_kepemilikan,var1


# F03. Login
def login():
    global login_count, login_status
    if login_status == False:
        # Melakukan login user dan mencatat posisi pada list user.csv
        login_username = str(input("Masukkan username: "))
        login_password = str(input("Masukkan password: "))
        username_found = False
        for i in range(len(username)):
            if login_username == username[i]:
                username_found = True
                if password[i] == login_password:
                    login_status = True
                    login_count = i
                    print("Selamat datang,",nama[login_count])
                    return login_status,login_count
                else:
                    print("Password atau username salah atau tidak ditemukan.")
                    break
        if username_found == False:
            print("Password atau username salah atau tidak ditemukan.")
    else:
        print("Anda sudah login. Silahkan exit jika ingin login kembali sebagai akun lain.")


# F02. Register

def register():
    global role,login_count,username,nama,password,saldo,row_user
    if login_status == True:
        if role[login_count] == "admin":
            register_nama = input("Masukkan nama: ")
            register_username = input("Masukkan username: ")
            while validitas_username(register_username) == False:
                print("Username hanya boleh memiliki huruf besar dan kecil, angka, spasi, strip(-), dan underscore(_).")
                register_username = input("Masukkan username: ") 
            register_password = input("Masukkan password: ")

            username_used = False
            for i in range(len(username)):
                if register_username == username[i]:
                    print("Username terpakai. Silahkan menggunakan username lain.")
                    username_used = True
                    break
            if username_used == False:
                namatemp = [register_nama]
                nama += namatemp
                usernametemp = [register_username]
                username += usernametemp
                passwordtemp = [register_password]
                password += passwordtemp
                role += ["user"]
                saldo += [0]
                row_user += 1
                print("Username",register_username,"telah berhasil register ke dalam “Binomo”.")
        else:
            print("Hanya admin yang dapat mengakses fitur ini.")
    else:
        print("Silahkan login sebelum menggunakan fitur ini.")

# F04. Menambah game ke toko game
def tambah_game():
    global role,login_count,id_game,nama_game,kategori_game,tahun_rilis,harga,stok,row_game
    if login_status == True:
        if role[login_count] == "admin":
            nama_game_baru = input("Masukkan nama game: ")
            kategori_game_baru = input("Masukkan kategori: ")
            tahun_rilis_baru = input("Masukkan tahun rilis: ")
            valid_input(tahun_rilis_baru,"Tahun rilis","tahun rilis")
            harga_baru = input("Masukkan harga: ")
            valid_input(harga_baru,"Harga","harga")
            stok_baru = input("Masukkan stok awal: ")
            valid_input(stok_baru,"Stok awal","stok awal")
            while nama_game_baru == "" or kategori_game_baru == "" or tahun_rilis_baru == "" or harga_baru == "" or stok_baru == "": 
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
                nama_game_baru = input("Masukkan nama game: ")
                kategori_game_baru = input("Masukkan kategori: ")
                tahun_rilis_baru = input("Masukkan tahun rilis: ")
                valid_input(tahun_rilis_baru,"Tahun rilis","tahun rilis")
                harga_baru = input("Masukkan harga: ")
                valid_input(harga_baru,"Harga","harga")
                stok_baru = input("Masukkan stok awal: ")
                valid_input(stok_baru,"Stok awal","stok awal")
            nomor_game = ""
            if (row_game%1000) <10:
                nomor_game += "00"+str(row_game%1000)
            elif (row_game%1000)<100:
                nomor_game += "0" + str(row_game%1000)
            else:
                nomor_game += str(row_game%1000)
            id_game_baru = "GAME" + nomor_game
            id_game += [id_game_baru]
            nama_game += [nama_game_baru]
            kategori_game += [kategori_game_baru]
            tahun_rilis += [tahun_rilis_baru]
            harga += [harga_baru]
            stok += [stok_baru]
            row_game += 1
            print("Selamat! Telah menambahkan game", nama_game_baru)
        else:
            print("Hanya admin yang dapat menambahkan game baru.")
    else:
        print("Fitur ini membutuhkan akses login.")

# F05. Mengubah game
def ubah_game():
    global login_status,role,login_count,id_game,nama_game,kategori_game,tahun_rilis,harga,stok,id_game_riwayat,nama_game_riwayat,harga_riwayat
    if login_status == True:
        if role[login_count] == "admin":
            id_game_ubah = input("Masukkan id game: ")
            nama_game_ubah = input("Masukkan nama game: ")
            kategori_game_ubah = input("Masukkan kategori: ")
            tahun_rilis_ubah = input("Masukkan tahun rilis: ")
            valid_input(tahun_rilis_ubah,"Tahun rilis","tahun rilis")
            harga_ubah = input("Masukkan harga: ")
            valid_input(harga_ubah,"Harga","harga")
            id_game_found = False
            for i in range(row_game):
                if id_game_ubah == id_game[i]:
                    id_game_found = True
                    if nama_game_ubah != "":
                        nama_game[i] = nama_game_ubah
                    if kategori_game_ubah != "":
                        kategori_game[i] = kategori_game_ubah
                    if tahun_rilis_ubah != "":
                        tahun_rilis[i] = tahun_rilis_ubah
                    if harga_ubah != "":
                        harga[i] = harga_ubah
                    break
            if id_game_found == True:
                for i in range(row_riwayat):
                    if id_game_ubah == id_game_riwayat[i]:
                        if nama_game_ubah != "":
                            nama_game_riwayat[i] = nama_game_ubah
                        if harga_ubah != "":
                            harga_riwayat[i] = harga_ubah
            else:
                print("Id game tidak ditemukan")
        else:
            print("Hanya admin yang dapat mengubah game")
    else:
        print("Fitur ini memerlukan login.")

# F06. Mengubah stok game
def ubah_stok():
    global login_status,role,login_count,stok,id_game,nama_game
    if login_status == True:
        if role[login_count] == "admin":
            stok_id_game = input("Masukkan id game: ")
            stok_ubah = input("Masukkan jumlah: ")
            valid_input(stok_ubah,"Stok","jumlah")
            id_game_found = False
            for i in range(row_game):
                if stok_id_game == id_game[i]:
                    id_game_found = True
                    if (int(stok[i]) + int(stok_ubah))>= 0:
                        stok[i] = int(stok[i]) + int(stok_ubah)
                        print("Selamat, stok game",nama_game[i],"sudah diupdate.")
                    else:
                        print("Stok game tidak bisa negatif")
            if id_game_found == False:
                print("Id game tidak ditemukan")
        else:
            print("Fitur ini hanya dapat diakses oleh admin.")
    else:
        print("Fitur perlu akses login")

# F07. Listing game
def sort_ascending(obj,obj2,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort):
    global row_game
    for j in range(1,row_game):
        count_min = j
        for i in range(j+1,row_game):
            if obj[i]<obj[count_min]:
                count_min = i 
        if count_min != j:
            obj[j],obj[count_min] = obj[count_min],obj[j]
            nama_game_sort[j],nama_game_sort[count_min] = nama_game_sort[count_min],nama_game_sort[j]
            id_game_sort[j],id_game_sort[count_min] = id_game_sort[count_min],id_game_sort[j]
            obj2[j],obj2[count_min] = obj2[count_min],obj2[j]
            kategori_game_sort[j],kategori_game_sort[count_min] = kategori_game_sort[count_min],kategori_game_sort[j]
            stok_sort[j],stok_sort[count_min] = stok_sort[count_min],stok_sort[j]
    return obj,nama_game_sort,id_game_sort,obj2,kategori_game_sort,stok_sort 

def sort_descending(obj1,obj2,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort):
    global row_game
    for j in range(1,row_game):
        count_max = j
        for i in range(j+1,row_game):
            if obj1[count_max]<obj1[i]:
                count_max = i 
        obj1[j],obj1[count_max] = obj1[count_max],obj1[j]
        nama_game_sort[j],nama_game_sort[count_max] = nama_game_sort[count_max],nama_game_sort[j]
        id_game_sort[j],id_game_sort[count_max] = id_game_sort[count_max],id_game_sort[j]
        obj2[j],obj2[count_max] = obj2[count_max],obj2[j]
        kategori_game_sort[j],kategori_game_sort[count_max] = kategori_game_sort[count_max],kategori_game_sort[j]
        stok_sort[j],stok_sort[count_max] = stok_sort[count_max],stok_sort[j]
    return obj1,nama_game_sort,id_game_sort,obj2,kategori_game_sort,stok_sort   

def sorting(skema,nama_game_sort,tahun_rilis_sort,id_game_sort,harga_sort,kategori_game_sort,stok_sort):
    global tahun_rilis,nama_game,id_game,harga,kategori_game,stok
    if skema == "tahun+":
        sort_ascending(nama_game_sort,harga_sort,tahun_rilis_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "tahun-":
        sort_descending(nama_game_sort,harga_sort,tahun_rilis_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "harga+":
        sort_ascending(harga_sort,tahun_rilis_sort,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "harga-":
        sort_descending(harga_sort,tahun_rilis_sort,nama_game_sort,id_game_sort,kategori_game_sort,stok_sort)
    elif skema == "":
        return
    else:
        print("Skema sorting salah.")

def list_game_toko():
    global id_game, nama_game, harga,tahun_rilis, kategori_game,stok,login_status,row_game
    if login_status == True:
        print("Mengurutkan game di toko secara harga atau tahun rilis. Contoh skema: tahun+")
        skema_sorting = input("Skema sorting: ")
        tahun_rilis_sort = tahun_rilis
        nama_game_sort = nama_game
        id_game_sort = id_game
        harga_sort = harga
        kategori_game_sort = kategori_game
        stok_sort = stok
        sorting(skema_sorting,tahun_rilis_sort,nama_game_sort,id_game_sort,harga_sort,kategori_game_sort,stok_sort)
        for i in range(1,row_game):
            print(str(i)+"."+ id_game_sort[i]+" | "+ nama_game_sort[i],end = "") 
            for j in range(40 - length(nama_game_sort[i])):
                print(" ",end = "")
            print(" | "+harga_sort[i] + " | " + kategori_game_sort[i] + " | " + tahun_rilis_sort[i] + " | " + stok_sort[i])
    else:
        print("Fitur ini memerlukan akses login.")

# F08. Membeli game
def buy_game():
    global id_game,id_game_kepemilikan,id_user,user_id_kepemilikan,row_game,row_kepemilikan,login_count,login_status,role,saldo,stok,nama_game,id_game_riwayat,nama_game_riwayat,user_id_riwayat,harga_riwayat,tahun_beli
    id_game_beli = input("Masukkan ID Game: ")
    if login_status == True:
        if role[login_count] == "user":
            for i in range(row_game):
                found = False
                if id_game[i] == id_game_beli:
                    found = True
                    harga_game_beli = harga[i]
                    nama_game_beli = nama_game[i]
                    game_index = i
                    break
            if found == True:
                bought = False
                for i in range(row_kepemilikan):
                    if user_id_kepemilikan[i] == role[login_count] and id_game_kepemilikan[i] == id_game_beli:
                        bought = True
                        break
                if bought == True:
                    print("Anda sudah memiliki game ini")
                else:
                    if int(saldo[login_count]) - int(harga_game_beli) <0:
                        print("Saldo anda tidak cukup untuk membeli game tersebut!")
                    if int(stok[game_index]) == 0:
                        print("Maaf. Stok game sedang habis.")
                    else:
                        saldo[login_count] = int(saldo[login_count]) - int(harga_game_beli)
                        stok[game_index] = int(stok[game_index]) - 1
                        user_id_kepemilikan += [id_user[login_count]]
                        id_game_kepemilikan += [id_game_beli]
                        id_game_riwayat += [id_game_beli]
                        harga_riwayat += [harga_game_beli]
                        user_id_riwayat += [id_user[login_count]]
                        nama_game_riwayat += [nama_game_beli]
                        tahun_beli += [2022] # Diganti per tahun 
                        print("Selamat.",nama_game_beli,"berhasil dibeli!")
            else:
                print("Game tidak ditemukan")
        else:
            print("Admin tidak bisa membeli game")
    else:
        print("Fitur ini memerlukan akses login")

# F09. Melihat game yang dimiliki

def list_game():
    global row_kepemilikan, id_game_kepemilikan, user_id_kepemilikan,id_game,nama_game,kategori_game,tahun_rilis,harga,id_user,login_count,login_status

    if login_status == True:
        if role[login_count] == "user":
            game_owned = 0
            for i in range(row_kepemilikan):
                if user_id_kepemilikan[i] == id_user[login_count]:
                    print("Daftar game: ")
                    game_owned += 1
                    for j in range(row_game):
                        if id_game_kepemilikan[i] == id_game[j]:  
                            print(str(game_owned)+". "+id_game[j]+" | "+nama_game[j]+" | "+kategori_game[j]+" | "+str(tahun_rilis[j])+" | "+str(harga[j]))
            if game_owned == 0:
                print("Anda tidak membeli game. Ketika beli_game untuk membeli game.")
        else:
            print("Hanya user yang dapat menggunakan fitur ini.")
    else:
        print("Fitur ini memerlukan akses login.")

# F10. Mencari game yang dimiliki dari ID dan tahun rilis
def data_game(id_game_list,tahun_rilis_list,game_index):
    global row_kepemilikan, id_game_kepemilikan, user_id_kepemilikan,id_game,tahun_rilis,id_user,login_count

    for i in range(row_kepemilikan):
        if user_id_kepemilikan[i] == id_user[login_count]:
            for j in range(row_game):
                if id_game_kepemilikan[i] == id_game[j]:
                    id_game_list += [id_game[j]]
                    tahun_rilis_list += [tahun_rilis[j]]
                    game_index += [j]
    return id_game_list,tahun_rilis_list,game_index

def search_my_game():
    global role,login_count,login_status,id_game,id_game_kepemilikan,nama_game,tahun_rilis,harga,kategori_game
    if login_status == True:
        if role[login_count] == "user":
            id_game_list = []
            tahun_rilis_list = []
            game_index = []
            data_game(id_game_list,tahun_rilis_list,game_index)
            game_owned = len(game_index)
            id_game_search = input("Masukkan ID game yang ingin dicari: ")
            tahun_rilis_search = input("Masukkan tahun rilis game: ")
            found = False
            count = 0
            print("Daftar game yang memenuhi kriteria: ")
            if tahun_rilis_search == "":
                for i in range(game_owned):
                    if id_game_search == id_game_list[i]:
                        found = True
                        count+=1
                        print(str(count)+". "+id_game_list[i]+" | "+nama_game[game_index[i]]+" | "+str(harga[game_index[i]])+" | "+kategori_game[game_index[i]]+" | "+str(tahun_rilis_list[i]))
            elif id_game_search == "":
                for i in range(game_owned):
                    if tahun_rilis_search == tahun_rilis_list[i]:
                        found=True
                        count+=1
                        print(str(count)+". "+id_game_list[i]+" | "+nama_game[game_index[i]]+" | "+str(harga[game_index[i]])+" | "+kategori_game[game_index[i]]+" | "+str(tahun_rilis_list[i]))
            elif id_game_search == "" and tahun_rilis_search == "":
                found = True
                list_game()
            else:
                for i in range(game_owned):
                    if tahun_rilis_search == tahun_rilis_list[i] and id_game_search == id_game_list[i]:
                        found = True
                        count+=1
                        print(str(count)+". "+id_game_list[i]+" | "+nama_game[game_index[i]]+" | "+str(harga[game_index[i]])+" | "+kategori_game[game_index[i]]+" | "+str(tahun_rilis_list[i]))
            if found == False:
                print("Tidak ada game yang memenuhi kriteria.")
        else:
            print("Hanya user yang dapat mengakses fitur ini.")
    else:
        print("Fitur ini memerlukan akses login")

# F11. Mencari game di Toko

def search_game_at_store():
    global login_status,id_game,nama_game,harga,kategori_game,tahun_rilis,stok,row_game
    if login_status == True:
        id_game_search = input("Masukkan id game: ")
        nama_game_search = input("Masukkan nama game: ")
        harga_game_search = input("Masukkan harga game: ")
        kategori_game_search = input("Masukkan kategori game: ")
        tahun_rilis_search = input("Masukkan tahun rilis game: ")
        count = 0
        print("Game yang memenuhi kriteria: ")
        for i in range(row_game):
            match = True
            if length(id_game_search)>0:
                if id_game_search != id_game[i]:
                    match = False
            if length(nama_game_search)>0:
                if nama_game_search != nama_game[i]:
                    match = False
            if length(harga_game_search)>0:
                if harga_game_search != harga[i]:
                    match = False
            if length(kategori_game_search)>0:
                if kategori_game_search != kategori_game[i]:
                    match = False
            if length(tahun_rilis_search)>0:
                if tahun_rilis_search != tahun_rilis[i]:
                    match = False
            if match == True:
                count+=1
                print(str(count)+". "+id_game[i]+" | "+nama_game[i]+" | "+harga[i]+" | "+kategori_game[i]+" | "+tahun_rilis[i]+" | "+stok[i])
        if count == 0:
            print("Tidak ada yang memenuhi kriteria")
    else:
        print("Fitur ini memerlukan akses login.")

# F12. Top up saldo
def topup():
    global login_status,login_count,role,saldo,username
    if login_status == True:
        if role[login_count] == "admin":
            user_topup = input("Masukkan username: ")
            topup = input("Masukkan saldo yang ingin diberikan: ")
            if not(cek_int(topup)):
                print("Masukan tidak valid")
                return            
            found = False
            for i in range(row_user):
                if user_topup == username[i]:
                    found = True
                    if int(saldo[i]) + int(topup)<0:
                        print("Masukan tidak valid.")
                    else:
                        saldo[i] = int(saldo[i])+int(topup)
                        print("Topup berhasil. Saldo",username[i],"menjadi",str(saldo[i]))
            if found == False:
                print('Username "',user_topup,'" tidak ditemukan.')
        else:
            print("Hanya admin yang dapat mengakses fitur ini.")
    else:
        print("Fitur ini memerlukan akses login")

# F13. Melihat Riwayat Pembelian
def riwayat():
    global login_count,role,login_status,id_user,id_game,harga_riwayat,id_game_riwayat,user_id_riwayat,nama_game_riwayat,tahun_beli
    if login_status == True:
        if role[login_count] == "user":
            print("Daftar game: ")
            count = 0
            for i in range(row_riwayat):
                if id_user[login_count] == user_id_riwayat[i]:
                    count += 1
                    print(str(count)+". "+id_game_riwayat[i]+" | "+nama_game_riwayat[i],end="")
                    for j in range(40-length(nama_game_riwayat[i])):
                        print(" ",end="")
                    print(" | "+str(harga_riwayat[i]),end = "")
                    for j in range(10-int(length(harga_riwayat[i]))):
                        print(" ",end="")
                    print(" | "+str(tahun_beli[i])+" |")
            if count == 0:
                print("Anda tidak memiliki game. Ketik beli_game untuk membeli.")
        else:
            print("Hanya user yang dapat melihat riwayat pembelian.")
    else:
        print("Fitur ini memerlukan akses login")
    
# F13. Help
def help():
    global login_status,role,login_count
    if login_status == True:
        print("===========   HELP   ===========")
        if role[login_count] == "admin":
            print("1. register - Melakukan registrasi user baru")
            print("2. login - Melakukan login ke dalam sistem")
            print("3. tambah_game -  Menambah game ke dalam toko")
            print("4. ubah_game - Mengubah properti game pada toko")
            print("5. ubah_stok - Mengubah stok game dalam toko")
            print("6. list_game_toko - Melihat semua game di dalam toko dan melakukan sorting")
            print("7. search_game_at_store - Mencari game di toko dengan parameter opsional")
            print("8. topup - Topup saldo user tertentu")
            print("9. save - Menyimpan hasil aktivitas dalam program")
            print("10. exit - Keluar dari program")
        else:
            print("1. login - Melakukan login dalam sistem.")
            print("2. list_game_toko - Melihat daftar game di toko dan melakukan sorting")
            print("3. buy_game - Membeli game di toko jika stok dan saldo mencukupi")
            print("4. list_game - Melihat game yang dimiliki")
            print('5. search_my_game - Mencari game yang dimiliki')
            print("6. search_game_at_store - Mencari game di toko game dengan paramter opsional")
            print("7. riwayat - Melihat riwayat pembelian game")
            print("8. save - Menyimpan hasil aktivitas dalam program")
            print("9. exit - Keluar dari program")
    else:
        print("Fitur ini memerlukan akses login")

# F15. Load

# Inisialisasi parsing file user.csv
data_path = os.path.join(current_dir,args.datafolder,"user.csv")
with open(data_path,'r') as f:
    row_user = count_row(f)
    row_game = 0
    row_user_temp = row_user
    id_user = [0 for i in range(row_user)]
    username = [0 for i in range(row_user)]
    nama = [0 for i in range(row_user)]
    password = [0 for i in range(row_user)]
    role = [0 for i in range(row_user)]
    saldo = [0 for i in range(row_user)]
    parsing_file1(f,id_user,username,nama,password,role,saldo)

# Inisialisasi parsing file game.csv
data_path = os.path.join(current_dir,args.datafolder,"game.csv")
with open(data_path,'r') as f:
    row_game = count_row(f)
    row_user = 0
    id_game = [0 for i in range(row_game)]
    nama_game = [0 for i in range(row_game)]
    kategori_game = [0 for i in range(row_game)]
    tahun_rilis = [0 for i in range(row_game)]
    harga = [0 for i in range(row_game)]
    stok = [0 for i in range(row_game)]
    parsing_file1(f,id_game,nama_game,kategori_game,tahun_rilis,harga,stok)
row_user = row_user_temp

# Inisialisasi parsing file riwayat.csv
data_path = os.path.join(current_dir,args.datafolder,"riwayat.csv")
with open(data_path,'r') as f:
    row_riwayat = count_row(f)
    id_game_riwayat = [0 for i in range(row_riwayat)]
    nama_game_riwayat = [0 for i in range(row_riwayat)]
    harga_riwayat = [0 for i in range(row_riwayat)]
    user_id_riwayat = [0 for i in range(row_riwayat)]
    tahun_beli = [0 for i in range(row_riwayat)]
    parsing_file2(id_game_riwayat,nama_game_riwayat,harga_riwayat,user_id_riwayat,tahun_beli)

# Inisialisasi parsing file kepemilikan.csv
data_path = os.path.join(current_dir,args.datafolder,"kepemilikan.csv")
with open(data_path,'r') as f:
    row_kepemilikan = count_row(f)
    id_game_kepemilikan = [0 for i in range(row_kepemilikan)]
    user_id_kepemilikan = [0 for i in range(row_kepemilikan)]
    parsing_file3(id_game_kepemilikan,user_id_kepemilikan)

# F16. Save


# Algoritma Utama
login_count = -1 # Menandakan belum login sehingga tidak ada posisi di list
login_status = False # Menandakan belum login

perintah = input("Selamat datang di BNMO! Apa yang ingin kamu lakukan hari ini? Ketik help untuk melihat semua perintah yang ada\n")
while True:
    if perintah.lower() == "login":
        login()
    elif perintah.lower() == "register":
        register()
    elif perintah.lower() == "tambah_game":
        tambah_game()
    elif perintah.lower() == "ubah_game":
        ubah_game()
    elif perintah.lower() == "ubah_stok":
        ubah_stok()
    elif perintah.lower() == "list_game_toko":
        list_game_toko()
    elif perintah.lower() == "buy_game":
        buy_game()
    elif perintah.lower() == "list_game":
        list_game()
    elif perintah.lower() == "search_my_game":
        search_my_game()
    elif perintah.lower() == "search_game_at_store":
        search_game_at_store()
    elif perintah.lower() == "topup":
        topup()
    elif perintah.lower() == "riwayat":
        riwayat()
    elif perintah.lower() == "help":
        help()
    perintah = input("Apa yang ingin kamu lakukan hari ini? Ketik help untuk melihat semua perintah yang ada \n")
