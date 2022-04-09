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
        while i<length(line):
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
        while i<length(line):
            if line[i] !=";":
                var1[count]+=line[i]
                i+=1
            else:
                break
        count+=1
    return id_game_kepemilikan,var1


# F02. Login

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


# F01. Register
def register():
    global role,login_count,username,nama,password
    if login_status == True:
        if role[login_count] == "admin":
            register_nama = input("Masukkan nama: ")
            register_username = input("Masukkan username: ")
            register_password = input("Masukkan password: ")
            username_used = False
            for i in range(row_user):
                if register_username == username[i]:
                    print("Username terpakai. Silahkan menggunakan username lain.")
                    username_used = True
            if username_used == False:
                namatemp = [register_nama]
                nama += namatemp
                usernametemp = [register_username]
                username += usernametemp
                passwordtemp = [register_password]
                password += passwordtemp
                print("Username",register_username,"telah berhasil register ke dalam “Binomo”.")
                print(username)
        else:
            print("Hanya admin yang dapat mengakses fitur ini.")
    else:
        print("Silahkan login sebelum menggunakan fitur ini.")

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
    if (perintah == "login" or perintah == "Login" or perintah == "LOGIN"):
        login()
    elif (perintah == "Register" or perintah == "REGISTER" or perintah == "register"):
        register()
    perintah = input("Apa yang ingin kamu lakukan hari ini? Ketik help untuk melihat semua perintah yang ada \n")
