# Tubes Daspro


# Kamus
# File yang digunakan pada code


file_user = open("user.csv","r")
file_game = open("game.csv","r")
file_riwayat = open("riwayat.csv","r")
file_kepemilikan = open("kepemilikan.csv","r")

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

    file_user = open(file,'r')
    Lines = file_user.readlines()
    
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
        while i<(length(line)-2):
            if line[i] !=";":
                var5[count]+=line[i]
                i+=1
            else:
                break
        count+=1
    return id,var1,var2,var3,var4,var5

def parsing_file2(id_game_riwayat,var1,var2,var3,var4):
    # Subprogram untuk menginisialisasi file riwayat.csv

    file_riwayat = open('riwayat.csv','r')
    Lines = file_riwayat.readlines()
    
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
        while i<(length(line)-2):
            if line[i] !=";":
                var4[count]+=line[i]
                i+=1
            else:
                break
        count+=1
    return id_game_riwayat,var1,var2,var3,var4

def parsing_file3(id_game_kepemilikan,var1):
    # Subprogram untuk menginisialisasi file riwayat.csv

    file_kepemilikan = open('kepemilikan.csv','r')
    Lines = file_kepemilikan.readlines()
    
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
        while i<(length(line)-2):
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
            nama_game += [nama_game_baru]
            kategori_game += [kategori_game]
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
    global login_status,role,login_count,stok,id_game
    if login_status == True:
        if role[login_count] == "admin":
            stok_id_game = input("Masukkan id game: ")
            stok_ubah = input("Masukkan jumlah: ")
            id_game_found = False
            for i in range(row_game):
                if stok_id_game == id_game[i]:
                    id_game_found = True
                    if (stok[i] - stok_ubah)>=0:
                        stok[i] -= stok_ubah
                    else:
                        print("Stok game tidak bisa negatif")
            if id_game_found == False:
                print("Id game tidak ditemukan")
        else:
            print("Fitur ini hanya dapat diakses oleh admin.")
    else:
        print("Fitur perlu akses login")




# Inisialisasi parsing file user.csv
row_user = count_row(file_user)
id_user = [0 for i in range(row_user)]
username = [0 for i in range(row_user)]
nama = [0 for i in range(row_user)]
password = [0 for i in range(row_user)]
role = [0 for i in range(row_user)]
saldo = [0 for i in range(row_user)]
parsing_file1("user.csv",id_user,username,nama,password,role,saldo)

# Inisialisasi parsing file game.csv
row_game = count_row(file_game)
id_game = [0 for i in range(row_game)]
nama_game = [0 for i in range(row_game)]
kategori_game = [0 for i in range(row_game)]
tahun_rilis = [0 for i in range(row_game)]
harga = [0 for i in range(row_game)]
stok = [0 for i in range(row_game)]
parsing_file1("game.csv",id_game,nama_game,kategori_game,tahun_rilis,harga,stok)

# Inisialisasi parsing file riwayat.csv
row_riwayat = count_row(file_riwayat)
id_game_riwayat = [0 for i in range(row_riwayat)]
nama_game_riwayat = [0 for i in range(row_riwayat)]
harga_riwayat = [0 for i in range(row_riwayat)]
user_id_riwayat = [0 for i in range(row_riwayat)]
tahun_beli = [0 for i in range(row_riwayat)]
parsing_file2(id_game_riwayat,nama_game_riwayat,harga_riwayat,user_id_riwayat,tahun_beli)

# Inisialisasi parsing file kepemilikan.csv
row_kepemilikan = count_row(file_kepemilikan)
id_game_kepemilikan = [0 for i in range(row_kepemilikan)]
user_id_kepemilikan = [0 for i in range(row_kepemilikan)]
parsing_file3(id_game_kepemilikan,user_id_kepemilikan)

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
        
    perintah = input("Apa yang ingin kamu lakukan hari ini? Ketik help untuk melihat semua perintah yang ada \n")
