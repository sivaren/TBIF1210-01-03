'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''
# F01 - Register
def reg():
    countuser = 1
    idcount = len(user)
    lanjut= True
    while countuser > 0 and lanjut==True:
        countuser = 0
        nama = input("Masukkan nama: ")
        usern = input("Masukkan username: ")
        passw = input("Masukkan password: ")
        almt = input("Masukkan alamat: ")

        for lines in range(len(user)):
            if user[lines]['username'] == usern:
                countuser +=1
                print()
                print("Username sudah terdaftar dan tidak dapat digunakan. ", end='')
                Y = input("Apakah anda ingin input ulang? (Y/N): ").upper()
                if Y == 'Y':
                    lanjut = True
                else : 
                    lanjut = False
                    return 0
    print() 
    print("User",usern,"telah berhasil register ke dalam Kantong Ajaib.")

    user_Dict = {}
    user_Dict['id'] = str(idcount+1)
    user_Dict['username'] = usern
    user_Dict['nama'] = nama
    user_Dict['alamat'] = almt
    user_Dict['pass'] = passw
    user_Dict['role'] = "user"

    user.append(user_Dict)    
