# Tubes Daspro : Program BNMO (Melakukan fitur-fitur pada BNMO)

# Kamus
# Import library
import argparse
import os
from functions import *
# Daftar fungsi dan prosedur


# Inisialisasi mengubah semua csv menjadi list
def parsing_file1(file,id,var1,var2,var3,var4,var5):
    # Subprogram untuk menginisialisasi file user.csv dan game.csv
    
    # Kamus Lokal
    # count,i : int
    # id,var1,var2,var3,var4,var5: array of string
    global row_user,row_game
    with open(data_path,'r') as f:
        Lines = f.readlines()
    
    # Algoritma
    count = 0               # Inisialisasi orde pada list
    for line in Lines:      # Iterasi sepanjang list
        id[count] = ""      # Pengosongan data pada list yang awalnya 0
        i = 0
        while i<length(line):           # Penginputan data pertama ke dalam list
            if line[i] !=";":
                id[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var1[count] = ""                
        while i<length(line):           # Penginputan data kedua ke dalam list
            if line[i] !=";":
                var1[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var2[count] = ""
        while i<length(line):           # Penginputan data ketiga dalam list
            if line[i] !=";":
                var2[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var3[count] = ""
        while i<length(line):           # Penginputan data keempat dalam list
            if line[i] !=";":
                var3[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var4[count] = ""
        while i<length(line):           # Penginputan data kelima ke dalam list
            if line[i] !=";":
                var4[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var5[count] =  ""               # Penginputan data keenam dalam list
        if count != (row_user-1) and count != (row_game-1):     # Jika bukan row terakhir \n dihapus dari elemen
            while i<(length(line)-1):
                if line[i] !=";":
                    var5[count]+=line[i]
                    i+=1
                else:
                    break
        elif count == (row_user-1) or count == (row_game-1):    # Jika row terakhir maka harus berbeda agar karakter terakhir tidak dihapus
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
    # Mirip seperti parsing_file1 hanya saja digunakan 5 parameter

    # Kamus Lokal
    # count, i : int
    # id_game_riwayat,var1,var2,var3,var4: array of string
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
    # Seperti parsing_file1 dan 2 tetapi hanya menggunakan 2 paramter

    # Kamus Lokal
    # count,i : int
    # id_game_kepemilikan,var1: array of string
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
    # Melakukan login dan mengeluarkan pesan error jika sudah login

    # Kamus Lokal
    # login_username,login_password: string
    # username_found,login_status: Bool
    # login_count: int
    global login_count, login_status
    
    # Algoritma
    if login_status == False:
        # Input
        login_username = str(input("Masukkan username: "))
        login_password = str(input("Masukkan password: "))
        # Pencarian username
        username_found = False              # Inisialisasi
        for i in range(len(username)):
            if login_username == username[i]:   # Proses jika ditemukan username
                username_found = True
                if password[i] == login_password:   # Pengecekan password
                    login_status = True
                    login_count = i
                    print("Selamat datang,",nama[login_count])
                    return login_status,login_count
                else:                               # Error password salah
                    print("Password atau username salah atau tidak ditemukan.")
                    break
        if username_found == False:                 # Error username telah ditemukan
            print("Password atau username salah atau tidak ditemukan.")
    else:                                           # Error jika sudah login
        print("Anda sudah login. Silahkan exit jika ingin login kembali sebagai akun lain.")


# F02. Register

def register():
    # Melakukan register user sebagai admin

    # Kamus Lokal
    # register_nama,register_username: string
    global role,login_count,username,nama,password,saldo,row_user

    # Algoritma
    if login_status == True:
        if role[login_count] == "admin":
            # Input
            register_nama = input("Masukkan nama: ")
            register_username = input("Masukkan username: ")
            while validitas_username(register_username) == False:       # Pesan error username tidak sesuai
                print("Username hanya boleh memiliki huruf besar dan kecil, angka, spasi, strip(-), dan underscore(_).")
                register_username = input("Masukkan username: ")        # Pengulangan validitas
            register_password = input("Masukkan password: ")

            username_used = False                                       # Inisialisasi pengecekan apakah username terpakai
            for i in range(len(username)):
                if register_username == username[i]:                    
                    print("Username terpakai. Silahkan menggunakan username lain.")     # Pesan error username terpakai
                    username_used = True
                    break
            if username_used == False:                                  # Peregisteran user ke dalam list
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
        else:                                                       # Pesan error pengaksesan dengan role user
            print("Hanya admin yang dapat mengakses fitur ini.")
    else:                                                           # Pesan error pengaksesan tanpa login
        print("Silahkan login sebelum menggunakan fitur ini.")

# F04. Menambah game ke toko game
def tambah_game():
    # Menambah game ke toko sebagai admin

    # Kamus Lokal
    # nama_game_baru,kategori_game_baru,tahun_rilis_baru,harga_baru,stok_baru,nomor_game : string
    global role,login_count,id_game,nama_game,kategori_game,tahun_rilis,harga,stok,row_game
    
    # Algoritma
    if login_status == True:
        if role[login_count] == "admin":
            # Input
            nama_game_baru = input("Masukkan nama game: ")
            kategori_game_baru = input("Masukkan kategori: ")
            tahun_rilis_baru = input("Masukkan tahun rilis: ")
            valid_input(tahun_rilis_baru,"Tahun rilis","tahun rilis")
            harga_baru = input("Masukkan harga: ")
            valid_input(harga_baru,"Harga","harga")
            stok_baru = input("Masukkan stok awal: ")
            valid_input(stok_baru,"Stok awal","stok awal")
            # Pengulangan jika salah satu paramter kosong
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
            # Pembuatan id game baru
            nomor_game = ""
            if (row_game%1000) <10:
                nomor_game += "00"+str(row_game%1000)
            elif (row_game%1000)<100:
                nomor_game += "0" + str(row_game%1000)
            else:
                nomor_game += str(row_game%1000)
            id_game_baru = "GAME" + nomor_game
            # Penyimpanan ke dalam list
            id_game += [id_game_baru]
            nama_game += [nama_game_baru]
            kategori_game += [kategori_game_baru]
            tahun_rilis += [tahun_rilis_baru]
            harga += [harga_baru]
            stok += [stok_baru]
            row_game += 1
            print("Selamat! Telah menambahkan game", nama_game_baru)
        else:
            # Pesan error sebagai user
            print("Hanya admin yang dapat menambahkan game baru.")
    else:
        # Pesan error tanpa login
        print("Fitur ini membutuhkan akses login.")

# F05. Mengubah game
def ubah_game():
    # Mengubah parameter sebuah game sebagai admin

    # Kamus Lokal
    # id_game_ubah,nama_game_ubah,kategori_game_ubah,tahun_rilis_ubah,harga_ubah: string
    # id_game_found :Bool
    # i: int
    global login_status,role,login_count,id_game,nama_game,kategori_game,tahun_rilis,harga,stok,id_game_riwayat,nama_game_riwayat,harga_riwayat
    
    # Algoritma
    if login_status == True:
        if role[login_count] == "admin":
            # Input
            id_game_ubah = input("Masukkan id game: ")
            nama_game_ubah = input("Masukkan nama game: ")
            kategori_game_ubah = input("Masukkan kategori: ")
            tahun_rilis_ubah = input("Masukkan tahun rilis: ")
            valid_input(tahun_rilis_ubah,"Tahun rilis","tahun rilis")       # Fungsi cek validitas input integer
            harga_ubah = input("Masukkan harga: ")
            valid_input(harga_ubah,"Harga","harga")                         # Fungsi pengecekan validitas input integer
            id_game_found = False
            for i in range(row_game):
                if id_game_ubah == id_game[i]:                              # Jika id game ditemukan
                    id_game_found = True
                    if nama_game_ubah != "":                                # Pengubahan parameter game
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
                            nama_game_riwayat[i] = nama_game_ubah           # Mengubah nama pada riwayat
            else:
                print("Id game tidak ditemukan")                            # Pesan error jika id game tidak ditemukan
        else:
            print("Hanya admin yang dapat mengubah game")                   # Pesan error ubah game sebagai user
    else:
        print("Fitur ini memerlukan login.")                                # Pesan error ubah game tanpa login

# F06. Mengubah stok game
def ubah_stok():
    # Mengubah stok dari game sebagai admin

    # Kamus Lokal
    # stok_id_game,stok_ubah: string
    # id_game_found: Bool
    # i : int
    global login_status,role,login_count,stok,id_game,nama_game
    
    # Algoritma
    if login_status == True:
        if role[login_count] == "admin":
            # Input
            stok_id_game = input("Masukkan id game: ")
            stok_ubah = input("Masukkan jumlah: ")
            valid_input(stok_ubah,"Stok","jumlah")          # Validitas cek integer input
            id_game_found = False
            for i in range(row_game):
                if stok_id_game == id_game[i]:              # Pencarian game
                    id_game_found = True
                    if (int(stok[i]) + int(stok_ubah))>= 0:         # Pengubahan stok game
                        stok[i] = int(stok[i]) + int(stok_ubah)
                        print("Selamat, stok game",nama_game[i],"sudah diupdate.")
                    else:
                        print("Stok game tidak bisa negatif")       # Pesan error jika mencoba mengubah stok gam menjadi negatif
            if id_game_found == False:
                print("Id game tidak ditemukan")                    # Pesan error game tidak ditemukan
        else:
            print("Fitur ini hanya dapat diakses oleh admin.")      # Pesan error mengubah stok sebagai user
    else:
        print("Fitur perlu akses login")                            # Pesan error mengubah stok tanpa login

# F07. Listing game
def list_game_toko():
    # Mengeluarkan info semua game di toko dengan skema sortingannya

    # Kamus Lokal
    # skema: string
    # nama_game_sort,id_game_sort,kategori_game_sort,stok_sort: array of string
    # i: int
    global id_game, nama_game, harga,tahun_rilis, kategori_game,stok,login_status,row_game
    
    # Algoritma
    if login_status == True:
        print("Mengurutkan game di toko secara harga atau tahun rilis. Contoh skema: tahun+")
        # Input
        skema_sorting = input("Skema sorting: ")
        # Membuat list baru khusus untuk sorting
        tahun_rilis_sort = tahun_rilis
        nama_game_sort = nama_game
        id_game_sort = id_game
        harga_sort = harga
        kategori_game_sort = kategori_game
        stok_sort = stok
        sorting(skema_sorting,tahun_rilis_sort,nama_game_sort,id_game_sort,harga_sort,kategori_game_sort,stok_sort)
        for i in range(1,row_game):
            if sorting(skema_sorting,tahun_rilis_sort,nama_game_sort,id_game_sort,harga_sort,kategori_game_sort,stok_sort) == False:
                print('Skema sorting salah.')
                break
            else:
                print(str(i)+"."+ id_game_sort[i]+" | "+ nama_game_sort[i],end = "")        # Memprint hasil 
                for j in range(40 - length(nama_game_sort[i])):
                    print(" ",end = "")
                print(" | "+harga_sort[i],end ="") 
                for j in range(10 - length(harga_sort[i])):
                    print(" ",end = "")
                print(" | " + kategori_game_sort[i],end = "")
                for j in range(20 - length(kategori_game_sort[i])):
                    print(" ",end = "")
                print(" | " + tahun_rilis_sort[i] + " | " + stok_sort[i])
                sorting("",tahun_rilis_sort,nama_game_sort,id_game_sort,harga_sort,kategori_game_sort,stok_sort)
    else:
        print("Fitur ini memerlukan akses login.")

# F08. Membeli game
def buy_game():
    # Membeli game sebagai user

    # Kamus Lokal
    # i,game_index: int
    # id_game_beli : string
    # bought: Bool
    # harga_game_beli,nama_game_beli: string
    global id_game,id_game_kepemilikan,id_user,user_id_kepemilikan,row_game,row_kepemilikan,login_count,login_status,role,saldo,stok,nama_game,id_game_riwayat,nama_game_riwayat,user_id_riwayat,harga_riwayat,tahun_beli
    
    # Algoritma
    if login_status == True:
        if role[login_count] == "user":
            # Input
            id_game_beli = input("Masukkan ID Game: ")
            for i in range(row_game):
                found = False
                if id_game[i] == id_game_beli:          # Mnecari game di toko
                    found = True
                    harga_game_beli = harga[i]          # Penanda lokasi game
                    nama_game_beli = nama_game[i]
                    game_index = i
                    break
            if found == True:
                bought = False
                for i in range(row_kepemilikan):            # Mencari game di kepemilikan
                    if user_id_kepemilikan[i] == role[login_count] and id_game_kepemilikan[i] == id_game_beli:
                        bought = True
                        break
                if bought == True:      # Pesan error jika game sudah dimiliki
                    print("Anda sudah memiliki game ini")
                else:                   
                    if int(saldo[login_count]) - int(harga_game_beli) <0:       # Pesan error jika saldo tidak cukup
                        print("Saldo anda tidak cukup untuk membeli game tersebut!")
                    if int(stok[game_index]) == 0:
                        print("Maaf. Stok game sedang habis.")                  # Pesan error jika stok 0
                    else:
                        # Penambahan kepemilikan game ke database
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
            else:           # Pesan error game tidak ditemukan
                print("Game tidak ditemukan")
        else:               # Pesan error membeli game sebagai admin
            print("Admin tidak bisa membeli game")
    else:                   # Pesan error membeli tanpa login
        print("Fitur ini memerlukan akses login")

# F09. Melihat game yang dimiliki
def list_game():
    # Melihat semua game yang dimiliki sebagai user

    # Kamus Lokal
    # game_owned: int
    # i,j: int
    global row_kepemilikan, id_game_kepemilikan, user_id_kepemilikan,id_game,nama_game,kategori_game,tahun_rilis,harga,id_user,login_count,login_status

    # Algoritma
    if login_status == True:
        if role[login_count] == "user":
            game_owned = 0                  # Penanda berapa game yang dimiliki
            for i in range(row_kepemilikan):
                if user_id_kepemilikan[i] == id_user[login_count]:          # Mencari id user dalam data kepemilikan
                    print("Daftar game: ")
                    game_owned += 1
                    for j in range(row_game):
                        if id_game_kepemilikan[i] == id_game[j]:            # Pencarian id game pada data game.csv
                            print(str(game_owned)+". "+id_game[j]+" | "+nama_game[j],end = "")      # Print data
                            for k in range(40-length(nama_game[j])):
                                print(" ",end = "")
                            print(" | "+kategori_game[j],end = "")
                            for k in range(20 - length(kategori_game[i])):
                                print(" ",end = "")
                            print(" | "+str(tahun_rilis[j])+" | "+str(harga[j]))
            if game_owned == 0:         # Pesan error tidak ada game
                print("Anda tidak membeli game. Ketika beli_game untuk membeli game.")
        else:                           # Pesan error list game sebagai admin
            print("Hanya user yang dapat menggunakan fitur ini.")
    else:                               # Pesan error list game tanpa login
        print("Fitur ini memerlukan akses login.")

# F10. Mencari game yang dimiliki dari ID dan tahun rilis
def search_my_game():
    # Mencari game yang dimiliki user

    # Kamus Lokal
    # id_game_list,tahun_rilis_list: array of string
    #game_index: array of int
    # game_owned,i: int
    # id_game_search,tahun_rilis_search: string
    global role,login_count,login_status,id_game,id_game_kepemilikan,nama_game,tahun_rilis,harga,kategori_game
    
    # Algoritma
    if login_status == True:
        if role[login_count] == "user":
            id_game_list = []                       # Inisialisasi list
            tahun_rilis_list = []
            game_index = []
            data_game(id_game_list,tahun_rilis_list,game_index)         # Pendataan game yang dimiliki user
            game_owned = len(game_index)
            # Input
            id_game_search = input("Masukkan ID game yang ingin dicari: ")
            tahun_rilis_search = input("Masukkan tahun rilis game: ")
            found = False
            count = 0
            print("Daftar game yang memenuhi kriteria: ")
            if tahun_rilis_search == "":                # Pencarian berdasarkan id game
                for i in range(game_owned):
                    if id_game_search == id_game_list[i]:
                        found = True
                        count+=1
                        print(str(count)+". "+id_game_list[i]+" | "+nama_game[game_index[i]]+" | "+str(harga[game_index[i]])+" | "+kategori_game[game_index[i]]+" | "+str(tahun_rilis_list[i]))
            elif id_game_search == "":                  # Pencarian berdasarkan tahun rilis
                for i in range(game_owned):
                    if tahun_rilis_search == tahun_rilis_list[i]:
                        found=True
                        count+=1
                        print(str(count)+". "+id_game_list[i]+" | "+nama_game[game_index[i]]+" | "+str(harga[game_index[i]])+" | "+kategori_game[game_index[i]]+" | "+str(tahun_rilis_list[i]))
            elif id_game_search == "" and tahun_rilis_search == "":
                found = True                             # Tanpa parameter, maka hanya list game
                list_game()
            else:
                for i in range(game_owned):              # Pencarian dengan kedua parameter
                    if tahun_rilis_search == tahun_rilis_list[i] and id_game_search == id_game_list[i]:
                        found = True
                        count+=1
                        print(str(count)+". "+id_game_list[i]+" | "+nama_game[game_index[i]]+" | "+str(harga[game_index[i]])+" | "+kategori_game[game_index[i]]+" | "+str(tahun_rilis_list[i]))
            if found == False:                           # Pesan error tidak ditemukan game
                print("Tidak ada game yang memenuhi kriteria.")
        else:                                            # Pencarian game yang dimiliki oleh admin
            print("Hanya user yang dapat mengakses fitur ini.")
    else:                                                # Pesan error mencari game yang dimiliki tanpa login
        print("Fitur ini memerlukan akses login")

# F11. Mencari game di Toko

def search_game_at_store():
    # Mencari game di toko berdasarkan 5 parameter yang opsional

    # Kamus Lokal
    # id_game_search,nama_game_search,harga_game_search,kategori_game_search,tahun_rilis_search: string
    # match: Bool
    global login_status,id_game,nama_game,harga,kategori_game,tahun_rilis,stok,row_game
    
    # Algoritma
    if login_status == True:
        # Input
        id_game_search = input("Masukkan id game: ")
        nama_game_search = input("Masukkan nama game: ")
        harga_game_search = input("Masukkan harga game: ")
        kategori_game_search = input("Masukkan kategori game: ")
        tahun_rilis_search = input("Masukkan tahun rilis game: ")
        count = 0
        print("Game yang memenuhi kriteria: ")
        for i in range(row_game):
            match = True
            if length(id_game_search)>0:                # Pencarian berdasarkan id game
                if id_game_search != id_game[i]:
                    match = False
            if length(nama_game_search)>0:              # Pencarian berdasarkan nama game
                if nama_game_search != nama_game[i]:
                    match = False
            if length(harga_game_search)>0:             # Pencarian berdasarkan harga game
                if harga_game_search != harga[i]:
                    match = False
            if length(kategori_game_search)>0:          # Pencarian berdasarkan kategori game
                if kategori_game_search != kategori_game[i]:
                    match = False
            if length(tahun_rilis_search)>0:            # Pencarian berdasarkan tahun rilis
                if tahun_rilis_search != tahun_rilis[i]:
                    match = False
            if match == True:
                count+=1                                # output
                print(str(count)+". "+id_game[i]+" | "+nama_game[i],end = "")
                for j in range(40-length(nama_game[i])):
                    print(" ",end = "")
                print(" | "+harga[i],end = "")
                for j in range(10 - length(harga[i])):
                    print(" ",end = "")
                print(" | "+kategori_game[i],end = "")
                for j in range(20 - length(kategori_game[i])):
                    print(" ",end = "")
                print(" | "+tahun_rilis[i]+" | "+stok[i])
        if count == 0:              # Pesan error tidak ditemukan search
            print("Tidak ada yang memenuhi kriteria")
    else:                           # Pesan error search game tanpa login
        print("Fitur ini memerlukan akses login.")

# F12. Top up saldo
def topup():
    # Melakukan topup pada akun user sebagai admi

    # Kamus Lokal
    # user_topup,topup: string
    # found : Bool
    global login_status,login_count,role,saldo,username

    # Algoritma
    if login_status == True:
        if role[login_count] == "admin":
            # Input
            user_topup = input("Masukkan username: ")
            topup = input("Masukkan saldo yang ingin diberikan: ")
            if not(cek_int(topup)):
                print("Masukan tidak valid")            # Pesan error bukan integer pada topup
                return            
            found = False
            for i in range(row_user):
                if user_topup == username[i]:           # Pencarian username pada data
                    found = True
                    if int(saldo[i]) + int(topup)<0:
                        print("Masukan tidak valid.")       # Pesan error saldo negatif
                    else:
                        saldo[i] = int(saldo[i])+int(topup)     # Penambahan saldo user
                        print("Topup berhasil. Saldo",username[i],"menjadi",str(saldo[i]))      
            if found == False:
                print('Username "',user_topup,'" tidak ditemukan.')     # Pesan error tidak ditemukan username
        else:
            print("Hanya admin yang dapat mengakses fitur ini.")        # Pesan error topup sebagai user
    else:
        print("Fitur ini memerlukan akses login")                       # Pesan error topup tanpa login

# F13. Melihat Riwayat Pembelian
def riwayat():
    # Melihat riwayat pembelian sebagai user
    
    # Kamus Lokal
    # count: int
    # i,j: int
    global login_count,role,login_status,id_user,id_game,harga_riwayat,id_game_riwayat,user_id_riwayat,nama_game_riwayat,tahun_beli
    
    # Algoritma
    if login_status == True:
        if role[login_count] == "user":
            print("Daftar game: ")
            count = 0
            for i in range(row_riwayat):
                if id_user[login_count] == user_id_riwayat[i]:          # Pencarian semua id user di data riwayat
                    count += 1                                          # Penanda urutan
                    print(str(count)+". "+id_game_riwayat[i]+" | "+nama_game_riwayat[i],end="")     # Print game user
                    for j in range(40-length(nama_game_riwayat[i])):
                        print(" ",end="")
                    print(" | "+str(harga_riwayat[i]),end = "")
                    for j in range(10-int(length(harga_riwayat[i]))):
                        print(" ",end="")
                    print(" | "+str(tahun_beli[i])+" |")
            if count == 0:              # Pesan error jika user tidak memiliki game
                print("Anda tidak memiliki game. Ketik beli_game untuk membeli.")
        else:                           # Pesan error melihat riwayat sebagai admin
            print("Hanya user yang dapat melihat riwayat pembelian.")
    else:                               # Pesan error melihat riwayat tanpa login
        print("Fitur ini memerlukan akses login")
    
# F13. Help
def help():
    global login_status,role,login_count
    if login_status == True:
        print("===========   HELP   ===========")
        if role[login_count] == "admin":
            # List command admin
            print("1. register - Melakukan registrasi user baru")
            print("2. login - Melakukan login ke dalam sistem")
            print("3. tambah_game -  Menambah game ke dalam toko")
            print("4. ubah_game - Mengubah properti game pada toko")
            print("5. ubah_stok - Mengubah stok game dalam toko")
            print("6. list_game_toko - Melihat semua game di dalam toko dan melakukan sorting")
            print("7. search_game_at_store - Mencari game di toko dengan parameter opsional")
            print("8. topup - Topup saldo user tertentu")
            print("9. save - Menyimpan hasil aktivitas dalam program")
            print("10. tic_tac_toe - Bermain game tic tac toe")
            print("11. exit - Keluar dari program")
        else:
            # List command user
            print("1. login - Melakukan login dalam sistem.")
            print("2. list_game_toko - Melihat daftar game di toko dan melakukan sorting")
            print("3. buy_game - Membeli game di toko jika stok dan saldo mencukupi")
            print("4. list_game - Melihat game yang dimiliki")
            print('5. search_my_game - Mencari game yang dimiliki')
            print("6. search_game_at_store - Mencari game di toko game dengan paramter opsional")
            print("7. riwayat - Melihat riwayat pembelian game")
            print("8. save - Menyimpan hasil aktivitas dalam program")
            print("9. tic_tac_toe - Bermain game tic tac toe")
            print("9. exit - Keluar dari program")
    else:
        # List command tanpa login(kedua role)
            print("1. register - Melakukan registrasi user baru")
            print("2. login - Melakukan login ke dalam sistem")
            print("3. tambah_game -  Menambah game ke dalam toko")
            print("4. ubah_game - Mengubah properti game pada toko")
            print("5. ubah_stok - Mengubah stok game dalam toko")
            print("6. list_game_toko - Melihat semua game di dalam toko dan melakukan sorting")
            print("7. buy_game - Membeli game di toko jika stok dan saldo mencukupi")
            print("8. list_game - Melihat game yang dimiliki")
            print('9. search_my_game - Mencari game yang dimiliki')
            print("10. search_game_at_store - Mencari game di toko dengan parameter opsional")
            print("11. riwayat - Melihat riwayat pembelian game")
            print("12. topup - Topup saldo user tertentu")
            print("13. save - Menyimpan hasil aktivitas dalam program")
            print("14. tic_tac_toe - Bermain game tic tac toe")
            print("15. exit - Keluar dari program")

# F15. Load
# Melakukan loading folder dan mengtransfer data ke dalam list saat program dipanggil
parser = argparse.ArgumentParser()
parser.add_argument("datafolder",help = "Folder tempat data.csv")
args = parser.parse_args()
current_dir = os.getcwd()
found = False
# Keluar dari program jika folder tidak ditemukan
if not(os.path.isdir(args.datafolder)):
    print("Folder tidak ditemukan")
    quit()

# Inisialisasi parsing file user.csv
data_path = os.path.join(current_dir,args.datafolder,"user.csv")
# Penyimpanan data ke dalam list
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
# Penyimpanan data ke dalam list
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
# Penyimpanan data ke dalam list
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
# Penyimpanan data ke dalam list
with open(data_path,'r') as f:
    row_kepemilikan = count_row(f)
    id_game_kepemilikan = [0 for i in range(row_kepemilikan)]
    user_id_kepemilikan = [0 for i in range(row_kepemilikan)]
    parsing_file3(id_game_kepemilikan,user_id_kepemilikan)

# F16. Save
def save():
    # Menyimpan data di csv sesuai data path
    global login_status

    if login_status == True:
        # Penyimpanan file user.csv
        
        # Membuat folder baru
        args.datafolder = input("Dimanakah kamu ingin menyimpan file savenya? ")
        if not(os.path.isdir(args.datafolder)):
            os.makedirs(args.datafolder)

        data_path = os.path.join(current_dir,args.datafolder,"user.csv")
        with open(data_path,"w") as f:
            for i in range(row_user):
                if i != row_user-1:
                    write_user = id_user[i]+";"+username[i]+";"+nama[i]+";"+password[i]+";"+role[i]+";"+saldo[i]+"\n"
                else:
                    write_user = id_user[i]+";"+username[i]+";"+nama[i]+";"+password[i]+";"+role[i]+";"+saldo[i]
                f.writelines(write_user)
        # Penyimpanan file game.csv
        data_path = os.path.join(current_dir,args.datafolder,"game.csv")
        with open(data_path,"w") as f:
            for i in range(row_game):
                if i != row_game-1:
                    write_game = id_game[i]+";"+nama_game[i]+";"+kategori_game[i]+";"+tahun_rilis[i]+";"+harga[i]+";"+stok[i]+"\n"
                else:
                    write_game = id_game[i]+";"+nama_game[i]+";"+kategori_game[i]+";"+tahun_rilis[i]+";"+harga[i]+";"+stok[i]
                f.writelines(write_game)
        # Penyimpanan file kepemilikan.csv
        data_path = os.path.join(current_dir,args.datafolder,"kepemilikan.csv")
        with open(data_path,"w") as f:
            for i in range(row_kepemilikan):
                if i != row_kepemilikan-1:
                    write_kepemilikan = id_game_kepemilikan[i]+";"+user_id_kepemilikan[i]+"\n"
                else:
                    write_kepemilikan = id_game_kepemilikan[i]+";"+user_id_kepemilikan[i]
                f.writelines(write_kepemilikan)
        # Penyimpanan file kepemilikan.csv
        data_path = os.path.join(current_dir,args.datafolder,"riwayat.csv")
        with open(data_path,"w") as f:
            for i in range(row_riwayat):
                if i != row_riwayat-1:
                    write_riwayat = id_game_riwayat[i]+";"+nama_game_riwayat[i]+";"+harga_riwayat[i]+";"+user_id_riwayat[i]+";"+tahun_beli[i]+"\n"
                else:
                    write_riwayat = id_game_riwayat[i]+";"+nama_game_riwayat[i]+";"+harga_riwayat[i]+";"+user_id_riwayat[i]+";"+tahun_beli[i]
                f.writelines(write_riwayat)
        print("Data berhasil disimpan!")
    else:
        # Pesan error tanpa login
        print("Fitur ini memerlukan akses login")

# F17. Exit
def exit():
    # Melakukan exit dari program

    # Kamus lokal
    # save_command: string
    global login_status

    # Algoritma
    if login_status == True:
        save_command = input("Apakah Anda ingin melakukan save sebelum exit? (Y/N) ") # Input jika user ingin menyimpan data
        if save_command == "Y" or save_command == "y":
            save()              # Save jika user ingin menyimpan data
            quit()              # Keluar program
        if save_command == "N" or save_command == "n":
            quit()              # Langsung keluar program jika user tidak ingin menyimpan data
    else:
        quit()

# Bonus 3
# Tic Tac Toe
def input_tic_tac_toe(papan,pemain):
    # Proses menginput pemain pada grid tic tac toe

    # Kamua lokal
    # pemain = char
    # papan: array of array of char
    # x,y: it
    # valid_matrix,valid_int : Bool
    global x,y

    # Algoritma
    # Input
    print("Giliran pemain",pemain,": ")
    valid_matrix = False

    # Validasi input
    while not(valid_matrix):
        x = input("Masukkan komponen x(1-3): ")
        y = input("Masukkan komponen y(1-3): ")
        # Jika x atau y bukan int
        if not(cek_int(str(x))) or not(cek_int(str(y))):
            valid_int = False
        else:
            valid_int = True
        if valid_int == True:
            # Jika x dan y sesuai matriks 3x3
            if (1<=int(x)<=3):
                if (1<=int(y)<=3):
                    valid_matrix = True
                else:
                    valid_matrix = False
            else:
                valid_matrix = False
        else:
            valid_matrix = False
    x = int(x)
    y = int(y)
    return papan

def cek_grid(papan):
    # Mengecek jika grid yang diinput di papan tic tac toe sudah digunakan
    
    # Kamus Lokal
    # papan: array of array of char
    # x,y: int
    global x,y
    
    # Memeriksa jika grid tic tac toe sudah terisi
    if papan[x-1][y-1] == "O" or papan[x-1][y-1] == "X":
        return True
        
x,y = -1,-1
def tic_tac_toe():
    # Melaksanakan game tic tac toe

    # Kamus Lokal
    # papan: array of array of char
    # x,y: int
    # count: int
    global x,y

    # Algoritma
    if login_status == True:
        # Inisialisasi papan
        papan = [["#" for i in range(3)]for j in range(3)]
        # Input pemain x dan input ke dalam papan
        input_tic_tac_toe(papan,"X")
        papan[x-1][y-1] = "X"
        # Reset variabel x dan y
        x,y = 0,0
        # Memprint isi papan
        print_papan(papan)
        # Print count jika pada kasus permainan seri
        count = 0
        # Range 4 karena hanya ada 9 kali gerakan
        # 1 di atas tambah 2x4 = 9
        for i in range(4):
            # Penambahan count setiap kali loop diulang
            count+=1
            # Input O dan validasinya
            input_tic_tac_toe(papan,"O")
            # Jika grid inputan sudah terisi
            while cek_grid(papan):
                print("Grid sudah terisi")
                input_tic_tac_toe(papan,"O")
            # Input ke dalam papan
            papan[x-1][y-1] = "O"
            # Reset variabel
            x,y = 0,0
            print_papan(papan)
            # Cek kemenangan
            if winning_condition(papan,"O"):
                print("Selamat. Pemain O menang")
                break
            # Hal yang sama juga dilakukan pada pemain X
            input_tic_tac_toe(papan,"X")
            while cek_grid(papan):
                print("Grid sudah terisi")
                input_tic_tac_toe(papan,"X")
            papan[x-1][y-1] = "X"
            x,y = 0,0
            print_papan(papan)
            if winning_condition(papan,"X"):
                print("Selamat. Pemain X menang")
                break
        if count == 4:
            # Jika permainan seri
            print("Permainan berakhir seri.")
    else:   # Pesan error tic tac toe tanpa login
        print("Fitur ini memerlukan akses login")


# Algoritma Utama
login_count = -1 # Menandakan belum login sehingga tidak ada posisi di list
login_status = False # Menandakan belum login

perintah = input("Selamat datang di BNMO! Silahkan login terlebih dahulu untuk mendapat fitur-fitur BNMO!\n")
while True:                 # Pengulangan selama belum dilakukan exit
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
    elif perintah.lower() == "save":
        save()
    elif perintah.lower() == "exit":
        exit()
    elif perintah.lower() == "tic_tac_toe":
        tic_tac_toe()
    else:
        print("Perintah salah. Silahkan menginput ulang.")          # Pesan error salah perintah
    
    perintah = input("Apa yang ingin kamu lakukan hari ini? Ketik help untuk melihat semua perintah yang ada \n")       # Pengulangan perintah/saat login
