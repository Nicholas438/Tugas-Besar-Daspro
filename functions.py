
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

def length_sentence(sentence):
    # Menghitung panjang dari suatu string

    # Kamus Lokal
    # len : int
    # sentence: string

    # Algoritma
    len = 0
    sentence_list = []
    for i in sentence:
        sentence_list += [i]
    len = 0
    for i in sentence_list:
        len+=1
    return len

def length_list(list):
    len = 0
    for i in list:
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
    for i in range(length_sentence(username)):   # Iteritas sepanjang length username
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
    for i in range(length_sentence(number)):
        if not(48<=ord(number[i])<=57) and not(ord(number[i]) == 45):
            return False                # Jika salah satu karakter bukanlah nomor maka akan direturn False
    return True



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

# Untuk Bonus 2. Magic Conch Shell
def response_generator(n,a,c,m):
    n = (a*n+c)%(m)
    bit = n%7
    if bit == 0:
        print("Mungkin")
    elif bit == 1:
        print("Iya")
    elif bit == 2:
        print("Tidak")
    elif bit == 3:
        print("Bisa Jadi")
    elif bit == 4:
        print("Maaf Magic Conch Shell tidak tersedia. Silahkan membeli Game Pengosong Dompet biar Magic Conch Shell bisa \njajan")
    elif bit == 5:
        print("Tidak tahu")
    elif bit == 6:
        print("Magic Conch Shell lagi mager")
    return n