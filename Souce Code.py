# Tubes Daspro


# Kamus
# File yang digunakan pada code
file_user = open("user.csv","r")



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
def parsing_user(id,username,nama,password,role,saldo):
    # Subprogram untuk menginisialisasi file user.csv

    file_user = open("user.csv",'r')
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
        username[count] = ""
        while i<length(line):
            if line[i] !=";":
                username[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        nama[count] = ""
        while i<length(line):
            if line[i] !=";":
                nama[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        password[count] = ""
        while i<length(line):
            if line[i] !=";":
                password[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        role[count] = ""
        while i<length(line):
            if line[i] !=";":
                role[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        saldo[count] =  ""
        while i<(length(line)-1):
            if line[i] !=";":
                saldo[count]+=line[i]
                i+=1
            else:
                break
        count+=1
    return id,username,nama,password,role,saldo



def login():
    username = str(input("Masukkan username: ",end = ""))
    password = str(input("Masukkan password: ",end = ""))
    file_user = open("user.csv")
    username_found = False
    login_status = False
    while True:

        line = file_user.readlines()
        if not line:
            break
        
        for row in file_user:
            while line_username != username:
                line_username = ""
                count = 0
                row_count = row

                while count < length(line):
                    if line[count]!=";":
                        line_username+=line[count]
                        count+=1
                        i+=1
                    else:
                        break
                if line_username == username:
                    username_found = True
        if username_found == False:
            print("Tidak ditemukan username yang diinput.")
            return username_found,login_status
        else:
            count+=1


# Inisialisasi parsing file user.csv
row_user = count_row(file_user)
id = [0 for i in range(row_user)]
username = [0 for i in range(row_user)]
nama = [0 for i in range(row_user)]
password = [0 for i in range(row_user)]
role = [0 for i in range(row_user)]
saldo = [0 for i in range(row_user)]
parsing_user(id,username,nama,password,role,saldo)
