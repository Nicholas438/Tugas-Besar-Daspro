file_user = open("user.csv")
# Subprogram untuk menghitung jumlah baris dari file csv
def count_row(file_user):
    #Setting initial value of the counter to zero
    rowcount  = 0
    #iterating through the whole file
    for row in open("user.csv"):
        rowcount+= 1
    return rowcount


def parsing_user(file_user,id,username,nama,password,role,saldo):
    count = 0
    while True:
 
        # Get next line from file
        row = file_user.readline()
    
        # if line is empty
        # end of file is reached
        if not row:
            break
    
        id[count] = ""
        i = 0
        while i<len(row):
            if row[i] !=";":
                id[count]+=row[i]
                i+=1
            else:
                break
        i+=1
        username[count] = ""
        while i<len(row):
            if row[i] !=";":
                username[count]+=row[i]
                i+=1
            else:
                break
        i+=1
        nama[count] = ""
        while i<len(row):
            if row[i] !=";":
                nama[count]+=row[i]
                i+=1
            else:
                break
        i+=1
        password[count] = ""
        while i<len(row):
            if row[i] !=";":
                password[count]+=row[i]
                i+=1
            else:
                break
        i+=1
        role[count] = ""
        while i<len(row):
            if row[i] !=";":
                role[count]+=row[i]
                i+=1
            else:
                break
        i+=1
        saldo[count] =  ""
        while i<(len(row)-1):
            if row[i] !=";":
                saldo[count]+=row[i]
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

                while count < len(line):
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
id = [0 for i in range(count_row(file_user))]
username = [0 for i in range(count_row(file_user))]
nama = [0 for i in range(count_row(file_user))]
password = [0 for i in range(count_row(file_user))]
role = [0 for i in range(count_row(file_user))]
saldo = [0 for i in range(count_row(file_user))]
parsing_user(file_user,id,username,nama,password,role,saldo)

  
