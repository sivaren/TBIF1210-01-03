import os
import argparse
import datetime

# PROGRAM FINAL UNTUK DIJALANKAN #

### BEBERAPA PRIMITIF ###

## FUNGSI UNTUK KONVERSI DATA
# fs. utk konversi suatu baris menjadi array of data (sbg pengganti fs. split())
def convertLine_to_arrDat(line):
    arr_dat = []
    count = 0
    while count < len(line):
        if line[count] != ';':
            count += 1
        else:
            arr_dat.append(line[:count])
            line = line[count+1:]
            count = 0
    arr_dat.append(line)
    return arr_dat
# fs. utk mengubah suatu array menjadi value yang real (untuk gadget/consumable)
def arr_to_realValues(array_data):
    arr_ret = array_data[:]
    for i in range(len(array_data)):
        if (i == 3):
            arr_ret[i] = int(arr_ret[i])
    return arr_ret
# fs. utk mengubah array of data menjadi format data sesuai file .csv yang siap untuk ditulis
def convertDatas_to_string(header, item):
    global user_header, user
    global gadget_header, gadgets
    global cons_header, cons
    global gadgetBorr_header, gadgetBorr_history
    global gadgetRet_header, gadgetRet_history
    global consHistory_header, consumable_history

    if item == gadgets and header == gadget_header:
        string_for_csv1 = ";".join(gadget_header) + "\n"
        for arr_data in gadgets:
            string_for_csv1 += arr_data['id'] + ';'
            string_for_csv1 += arr_data['nama'] + ';'
            string_for_csv1 += arr_data['deskripsi'] + ';'
            string_for_csv1 += str(arr_data['jumlah']) + ';'
            string_for_csv1 += arr_data['rarity'] + ';'
            string_for_csv1 += arr_data['tahun_ditemukan'] + '\n'
        return string_for_csv1
    
    elif item == cons and header == cons_header:
        string_for_csv2 = ";".join(cons_header) + "\n"
        for arr_data in cons:
            string_for_csv2 += arr_data['id'] + ';'
            string_for_csv2+= arr_data['nama'] + ';'
            string_for_csv2+= arr_data['deskripsi'] + ';'
            string_for_csv2+= str(arr_data['jumlah']) + ';'
            string_for_csv2+= arr_data['rarity'] + '\n'
        return string_for_csv2

    elif item == user and header == user_header:
        string_for_csv3 = ";".join(user_header) + "\n"
        for arr_data in user:
            string_for_csv3 += arr_data['id'] + ';'
            string_for_csv3 += arr_data['username'] + ';'
            string_for_csv3 += arr_data['nama'] + ';'
            string_for_csv3 += arr_data['alamat'] + ';'
            string_for_csv3 += arr_data['pass'] + ';'
            string_for_csv3 += arr_data['role'] + '\n'
        return string_for_csv3
    
    elif item == gadgetBorr_history and header == gadgetBorr_header:
        string_for_csv4 = ";".join(gadgetBorr_header) + "\n"
        for arr_data in gadgetBorr_history:
            string_for_csv4 += arr_data['id'] + ';'
            string_for_csv4 += arr_data['id_peminjam'] + ';'
            string_for_csv4 += arr_data['id_gadget'] + ';'
            string_for_csv4 += arr_data['tanggal_peminjaman'] + ';'
            string_for_csv4 += str(arr_data['jumlah']) + ';' 
            string_for_csv4 += arr_data['is_returned'] + '\n'
        return string_for_csv4

    elif item == gadgetRet_history and header == gadgetRet_header:
        string_for_csv5 = ";".join(gadgetRet_header) + "\n"
        for arr_data in gadgetRet_history:
            string_for_csv5 += arr_data['id'] + ';'
            string_for_csv5 += arr_data['id_peminjaman'] + ';'
            string_for_csv5 += arr_data['tanggal_pengembalian'] + '\n'
        return string_for_csv5

    elif item == consumable_history and header == consHistory_header:
        string_for_csv6 = ";".join(consHistory_header) + "\n"
        for arr_data in consumable_history:
            string_for_csv6 += arr_data['id'] + ';'
            string_for_csv6 += arr_data['id_pengambil'] + ';'
            string_for_csv6 += arr_data['id_consumable'] + ';'
            string_for_csv6 += arr_data['tanggal_pengambilan'] + ';'
            string_for_csv6 += str(arr_data['jumlah']) + '\n'
        return string_for_csv6

## FUNGSI UNTUK PENGECEKAN
# fS. untuk mengecek validitas input ID (gadget dan consumable)
def isID_Valid(id):
    if id[0] == 'G':
        if len(id) <= 1: 
            return False
        else:
            return True
    elif id[0] == 'C':
        if len(id) <= 1: 
            return False
        else:
            return True
    else:
        return False
# fs. utk mengetahui keberadaan item, ada atau tidak pada suatu file .csv (untuk gadget/consumable)
def item_existence(id):
    alamat = which_item(id)
    for i in range(len(alamat)):
        if id == alamat[i]['id']:
            return True
            break
        elif i == len(alamat) - 1:
            return False
        else:
            continue
# fs. utk menentukan apakah suatu input gadget ataukah cons, dan mengembalikan array of gadgets/cons
def which_item(id):
    global gadgets, cons

    if id[0] == 'G':
        return gadgets
    elif id[0] == 'C':
        return cons
# fs. utk mencari item pd posisi tertentu, dan mengembalikan alamat dari item tsb (utk gadget/consumable)
def item_position(id):
    alamat = which_item(id)
    for i in range(len(alamat)):
        if id == alamat[i]['id']:
            return alamat[i]
            break
# fs. utk memvalidasi input tanggal
def is_tanggalValid(tgl):
    try:
        date_obj = datetime.datetime.strptime(tgl, '%d/%m/%Y')
        return True
    except ValueError:
        return False

## FUNGSI TERKAIT DENGAN TANGGAL
# fs. utk mengubah format tanggal menjadi suatu array yang terpisah -> [day, month, year]
def date_parser(array):
    if array == gadgetBorr_history:
        for i in range(len(array)):
            date = array[i]['tanggal_peminjaman']
            garing = "/"
            day = "" 
            month = ""
            year = ""
            for j in range(len(date)):
                day += date[j]
                if date[j+1] == garing:
                    for k in range(len(date)-(j+1)):
                        month += date[j+k+2]
                        if date[k+1] == garing:
                            for l in range(len(date)-(j+k+4)):
                                year += date [j+k+l+4]
                            break
                    break
            array[i]['tanggal_peminjaman'] = [day,month,year]
    elif array == gadgetRet_history:
        for i in range(len(array)):
            date = array[i]['tanggal_pengembalian']
            garing = "/"
            day = "" 
            month = ""
            year = ""
            for j in range(len(date)):
                day += date[j]
                if date[j+1] == garing:
                    for k in range(len(date)-(j+1)):
                        month += date[j+k+2]
                        if date[k+1] == garing:
                            for l in range(len(date)-(j+k+4)):
                                year += date [j+k+l+4]
                            break
                    break
            array[i]['tanggal_pengembalian'] = [day,month,year]
    elif array == consumable_history:
        for i in range(len(array)):
            date = array[i]['tanggal_pengambilan']
            garing = "/"
            day = "" 
            month = ""
            year = ""
            for j in range(len(date)):
                day += date[j]
                if date[j+1] == garing:
                    for k in range(len(date)-(j+1)):
                        month += date[j+k+2]
                        if date[k+1] == garing:
                            for l in range(len(date)-(j+k+4)):
                                year += date [j+k+l+4]
                            break
                    break
            array[i]['tanggal_pengambilan'] = [day,month,year]
    return array
# fs. utk sorting tanggal pada array gadgetBorr_history
def sorting_date_gadBorr(arr, x, arr_of_data):
    for i in range(len(arr)):
        if arr_of_data[x]['tanggal_peminjaman'][2] > arr[i]['tanggal_peminjaman'][2]:
            arr.insert(i,arr_of_data[x])
            break
        elif arr_of_data[x]['tanggal_peminjaman'][2] == arr[i]['tanggal_peminjaman'][2]:
            if arr_of_data[x]['tanggal_peminjaman'][1] > arr[i]['tanggal_peminjaman'][1]:
                arr.insert(i,arr_of_data[x])
                break
            elif arr_of_data[x]['tanggal_peminjaman'][1] == arr[i]['tanggal_peminjaman'][1]:
                if arr_of_data[x]['tanggal_peminjaman'][0] >= arr[i]['tanggal_peminjaman'][0]:
                    arr.insert(i,arr_of_data[x])
                    break
                elif i+1 == len(arr):
                    arr.append(arr_of_data[x])
                    break
                else :
                    continue
            elif i+1 == len(arr):
                arr.append(arr_of_data[x])
                break
            else :
                continue
        elif i+1 == len(arr):
            arr.append(arr_of_data[x])
            break
        else :
            continue
# fs. utk sorting tanggal pada array gadgetRet_history
def sorting_date_gadRet(arr, x, arr_of_data):
    for i in range(len(arr)):
        if arr_of_data[x]['tanggal_pengembalian'][2] > arr[i]['tanggal_pengembalian'][2]:
            arr.insert(i,arr_of_data[x])
            break
        elif arr_of_data[x]['tanggal_pengembalian'][2] == arr[i]['tanggal_pengembalian'][2]:
            if arr_of_data[x]['tanggal_pengembalian'][1] > arr[i]['tanggal_pengembalian'][1]:
                arr.insert(i,arr_of_data[x])
                break
            elif arr_of_data[x]['tanggal_pengembalian'][1] == arr[i]['tanggal_pengembalian'][1]:
                if arr_of_data[x]['tanggal_pengembalian'][0] >= arr[i]['tanggal_pengembalian'][0]:
                    arr.insert(i,arr_of_data[x])
                    break
                elif i+1 == len(arr):
                    arr.append(arr_of_data[x])
                    break
                else :
                    continue
            elif i+1 == len(arr):
                arr.append(arr_of_data[x])
                break
            else :
                continue
        elif i+1 == len(arr):
            arr.append(arr_of_data[x])
            break
        else :
            continue
# fs. utk sorting tanggal pada array consumable_history
def sorting_date_consHis(arr, x, arr_of_data):
    for i in range(len(arr)):
        if arr_of_data[x]['tanggal_pengambilan'][2] > arr[i]['tanggal_pengambilan'][2]:
            arr.insert(i,arr_of_data[x])
            break
        elif arr_of_data[x]['tanggal_pengambilan'][2] == arr[i]['tanggal_pengambilan'][2]:
            if arr_of_data[x]['tanggal_pengambilan'][1] > arr[i]['tanggal_pengambilan'][1]:
                arr.insert(i,arr_of_data[x])
                break
            elif arr_of_data[x]['tanggal_pengambilan'][1] == arr[i]['tanggal_pengambilan'][1]:
                if arr_of_data[x]['tanggal_pengambilan'][0] >= arr[i]['tanggal_pengambilan'][0]:
                    arr.insert(i,arr_of_data[x])
                    break
                elif i+1 == len(arr):
                    arr.append(arr_of_data[x])
                    break
                else :
                    continue
            elif i+1 == len(arr):
                arr.append(arr_of_data[x])
                break
            else :
                continue
        elif i+1 == len(arr):
            arr.append(arr_of_data[x])
            break
        else :
            continue
# fs. utk membalikan format tanggal dari array menjadi -> dd/mm/yyyy (utk gadgetBorr_history)
def balikin_tgl_gadBorr(arr):
    for i in range(len(arr)):
        date_str = ""
        date_str += arr[i]['tanggal_peminjaman'][0] + '/'
        date_str += arr[i]['tanggal_peminjaman'][1] + '/'
        date_str += arr[i]['tanggal_peminjaman'][2]
        arr[i]['tanggal_peminjaman'] = date_str
# fs. utk membalikan format tanggal dari array menjadi -> dd/mm/yyyy (utk gadgetRet_history)
def balikin_tgl_gadRet(arr):
    for i in range(len(arr)):
        date_str = ""
        date_str += arr[i]['tanggal_pengembalian'][0] + '/'
        date_str += arr[i]['tanggal_pengembalian'][1] + '/'
        date_str += arr[i]['tanggal_pengembalian'][2]
        arr[i]['tanggal_pengembalian'] = date_str
# fs. utk membalikan format tanggal dari array menjadi -> dd/mm/yyyy (utk consumable_history)
def balikin_tgl_consHis(arr):
    for i in range(len(arr)):
        date_str = ""
        date_str += arr[i]['tanggal_pengambilan'][0] + '/'
        date_str += arr[i]['tanggal_pengambilan'][1] + '/'
        date_str += arr[i]['tanggal_pengambilan'][2]
        arr[i]['tanggal_pengambilan'] = date_str

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

# F02 - Login
def login():
    global active_user
    global isRun

    usern = input("Masukkan username: ")
    passw = input("Masukkan password: ")
    print()
    isRun = True
    while active_user== {} and isRun == True:
        for i in range(len(user)):
            if usern == user[i]['username'] and passw == user[i]['pass']:
                print('''        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⠟⠫⢻⣿⣿⣿⣿⢟⣩⡍⣙⠛⢛⣿⣿⣿⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⡿⢿⣿
        ⣿⠤⠄⠄⠙⢿⣿⣿⣿⡿⠿⠛⠛⢛⣧⣿⠇⠄⠂⠄⠄⠄⠘⣿⣿⣿⣿⠁⠄⢻
        ⣿⣿⣿⣿⣶⣄⣾⣿⢟⣼⠒⢲⡔⣺⣿⣧⠄⠄⣠⠤⢤⡀⠄⠟⠉⣠⣤⣤⣤⣾
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣬⣵⣿⣿⣿⣶⡤⠙⠄⠘⠃⠄⣴⣾⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⢿⣿⣿⠿⠋⠁⠄⠂⠉⠒⢘⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⣷⣶⣤⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣷⣦⣰⠄⠄⠄⠄⢾⠿⢿⣿⣿⣿⣿
        ⣿⡿⠋⣡⣾⣿⣿⣿⡟⠉⠉⠈⠉⠉⠉⠉⠉⠄⠄⠄⠑⠄⠄⠐⡇⠄⠈⠙⠛⠋
        ⠋⠄⣾⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⡇⠄⠄⠄⠄⠄
        ⠄⢸⣿⣿⣿⣿⣿⣯⠄⢠⡀⠄⠄⠄⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄
        ⠁⢸⣿⣿⣿⣿⣿⣯⣧⣬⣿⣤⣐⣂⣄⣀⣠⡴⠖⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠈⠈⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣽⣉⡉⠉⠈⠁⠄⠁⠄⠄⠄⠄⡂⠄⠄⠄⠄⠄
        ⠄⠄⠙⣿⣿⠿⣿⣿⣿⣿⣷⡤⠈⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠠⠔⠄⠄⠄⠄⠄
        ⠄⠄⠄⡈⢿⣷⣿⣿⢿⣿⣿⣷⡦⢤⡀⠄⠄⠄⠄⠄⠄⢐⣠⡿⠁⠄⠄⠄⠄⠄
        ''')
                print("Halo, " + user[i]['username']+ "! Selamat datang di Kantong Ajaib.")
                active_user = user[i]
                print()
                break
        if active_user=={}:
            print("Username dan/atau Password Tidak Valid. ", end='')
            Y = input("Apakah anda ingin login ulang? (Y/N): ").upper()
            if Y=='Y':
                isRun = True
                usern = input("Masukkan username: ")
                passw = input("Masukkan password: ")
                print()
            else:
                print("")
                print("Selamat tinggal.")
                isRun = False
                return 0
    return active_user

# F03 - Pencarian gadget berdasarkan rarity
def carirarity():

    def print_gadget(i):
        print("Nama            :", gadgets[i]['nama'] )
        print("Deskripsi       :", gadgets[i]['deskripsi'])
        print("Jumlah          :", gadgets[i]['jumlah'], "buah")
        print("Rarity          :", gadgets[i]['rarity'])
        print("Tahun ditemukan :", gadgets[i]['tahun_ditemukan'])
        print()    


    rarity = input("Masukkan rarity: ").upper()                     #input sudah pasti valid
    print()
    print("Hasil Pencarian: ")
    print()
    for i in range(len(gadgets)):
        if rarity == gadgets[i]['rarity']:
            print_gadget(i)

# F04 - Pencarian gadget berdasarkan tahun ditemukan
def caritahun():

    def print_gadget(i):
    
        print("Nama            :", gadgets[i]['nama'] )
        print("Deskripsi       :", gadgets[i]['deskripsi'])
        print("Jumlah          :", gadgets[i]['jumlah'])
        print("Rarity          :", gadgets[i]['rarity'])
        print("Tahun ditemukan :", gadgets[i]['tahun_ditemukan'])
        print()    

    thn = int(input("Masukkan Tahun: "))
    ktg = input("Masukkan Kategori: ")
    print()
    print("Hasil Pencarian: ")
    print()
    if ktg == "<":
        for i in range(len(gadgets)):
            if int(gadgets[i]['tahun_ditemukan']) < thn:
                print_gadget(i)
    elif ktg == ">":
        for i in range(len(gadgets)):
            if int(gadgets[i]['tahun_ditemukan']) > thn:
                print_gadget(i)
    elif ktg == "=":
        for i in range(len(gadgets)):
            if int(gadgets[i]['tahun_ditemukan']) == thn:
                print_gadget(i)
    elif ktg == "<=":
        for i in range(len(gadgets)):
            if int(gadgets[i]['tahun_ditemukan']) <= thn:
                print_gadget(i)
    elif ktg == ">=":
        for i in range(len(gadgets)):
            if int(gadgets[i]['tahun_ditemukan']) >= thn:
                print_gadget(i)

# F05 - Menambah Item 
def tambahitem():
    error = False

    def CekAdaGadget(inputid):
        for i in range(len(gadgets)):
            if inputid == gadgets[i]['id']:
                return True
                break
    def CekAdaCons(inputid):
        for i in range(len(cons)):
            if inputid == cons[i]['id']:
                return True
                break

    inputid = input("Masukan ID: ")
    if not isID_Valid(inputid):
        print()
        print("Gagal menambahkan item karena ID tidak valid.")
        error = True
    elif CekAdaCons(inputid) or CekAdaGadget(inputid):
        print()
        print("Gagal menambahkan item karena ID sudah ada.")
        error = True
    else: 
        nama = input("Masukkan Nama: ")
        desk = input("Masukkan Deskripsi: ")
        juml = input("Masukkan Jumlah: ")
        if juml.isdecimal():
            rare = input("Masukkan Rarity: ")
            if rare == 'C' or rare == 'B' or rare == 'A' or rare == 'S':
                    if inputid[0] == 'G':
                        thn = input("Masukkan tahun ditemukan: ")
                        if thn.isdecimal():
                            print()
                            print("Item telah berhasil ditambahkan ke database.")

                        else :  
                            print()
                            print("Gagal menambahkan item karena Tahun Tidak Valid.")
                            error= True
                    else:
                        print()
                        print("Item telah berhasil ditambahkan ke database.")
            else : 
                print()
                print("Gagal menambahkan item karena rarity tidak valid.")
                error = True
        else :
            print()
            print("Gagal menambahkan item karena jumlah tidak valid.")
            error = True


    if error == False:
        addition_dict = {}
        addition_dict['id'] = inputid
        addition_dict['nama'] = nama
        addition_dict['deskripsi'] = desk
        addition_dict['jumlah'] = int(juml)
        addition_dict['rarity'] = rare
        if inputid[0] == 'G':
            addition_dict['tahun_ditemukan'] = thn
            gadgets.append(addition_dict)

        else:
            cons.append(addition_dict)
    else: 
        return 0

# F06 - Menghapus Gadget atau Consumable
def delete_item():
    id_item = input("Masukkan ID item: ")
    
    if isID_Valid(id_item):
        if item_existence(id_item):
            taken_from = which_item(id_item)
            the_item = item_position(id_item)
            item_idx = taken_from.index(the_item)

            qu = input(f"Apakah anda yakin ingin menghapus {the_item['nama']} (Y/N)? ").upper()
            if qu == 'Y':
                if taken_from == gadgets:
                    del gadgets[item_idx]

                elif taken_from == cons:
                    del cons[item_idx]                    

                print()
                print("Item telah berhasil dihapus dari database.")
            
            elif qu == 'N':
                print()
                print("Penghapusan item dibatalkan.")
        else:
            print()
            print("Tidak ada item dengan ID tersebut.")

    else:
        print()
        print("Input ID item tidak valid!")

# F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
def ubah_jumlah():
    id_item = input("Masukkan ID item: ")

    if isID_Valid(id_item):
        if item_existence(id_item):
            change_qty = int(input("Masukkan jumlah: "))
            taken_from = which_item(id_item)
            the_item = item_position(id_item)
            item_idx = taken_from.index(the_item)

            the_qty = int(the_item['jumlah'])
            now_qty = the_qty + change_qty

            if now_qty < 0 :
                print()
                print(f"{abs(change_qty)} {the_item['nama']} gagal dibuang karena stok kurang. Stok sekarang: {the_qty} (< {abs(change_qty)})")
            else:
                taken_from[item_idx]['jumlah'] = now_qty

                if now_qty > the_qty:
                    print()
                    print(f"{change_qty} {the_item['nama']} berhasil ditambah. Stok sekarang: {now_qty}")
                elif now_qty < the_qty:
                    print()
                    print(f"{abs(change_qty)} {the_item['nama']} berhasil dibuang. Stok sekarang: {now_qty}")
                else:
                    print()
                    print(f"Jumlah {the_item['nama']} tetap sama. Stok sekarang: {now_qty}")
        else:
            print()
            print("Tidak ada item dengan ID tersebut.")
    else:
        print()
        print("Input ID item tidak valid!")

# F08 - Meminjam Gadget
def pinjam_gadget():
    id = input("Masukkan ID item: ")
    
    if id[0] =='G' and len(id) > 1:
        if item_existence(id):

            line_item = item_position(id)
            item_idx = gadgets.index(line_item)
            the_item = gadgets[item_idx]
            item_qty = int(the_item['jumlah'])
            
            print("-------------------------------")
            print("*Format tanggal --> DD/MM/YYYY")
            tgl_pinjam = str(input("Tanggal peminjaman: "))

            if is_tanggalValid(tgl_pinjam):
                
                print("-------------------------------")
                jml_pinjam = int(input("Jumlah peminjaman (tidak boleh negatif): "))

                if jml_pinjam > 0:
                    if jml_pinjam > item_qty:
                        print()
                        print(f"{the_item['nama']} tidak dapat dipinjam karena stok kurang. Stok item: {item_qty} (< {jml_pinjam})")
                    else:
                        gadBorr_qty = len(gadgetBorr_history)

                        new_history = {
                            'id' : str(gadBorr_qty+1),
                            'id_peminjam' : active_user['id'], 
                            'id_gadget' : the_item['id'],
                            'tanggal_peminjaman' : tgl_pinjam,
                            'jumlah' : jml_pinjam,
                            'is_returned' : 'false'
                        }

                        gadgetBorr_history.append(new_history)

                        the_item['jumlah'] = item_qty - jml_pinjam

                        print()
                        print(f"Item {the_item['nama']} (x{jml_pinjam}) berhasil dipinjam!")
 
                elif jml_pinjam == 0:
                    print()
                    print("Anda tidak jadi meminjam item.")
                else:
                    print()
                    print("Input jumlah peminjaman tidak boleh negatif!")
            else:
                print()
                print("Input data tanggal tidak valid!")

        else:
            print()
            print("Tidak ada item dengan ID tersebut.")
    else:
        print()
        print("Input ID item tidak valid!")

# F09 - Mengembalikan Gadget
def balikin_gadget():
    gadBorr_history_userAct = []
    
    for line in gadgetBorr_history:
        if line['id_peminjam'] == active_user['id'] and line['is_returned'] == 'false':
            gadBorr_history_userAct.append(line)

    if len(gadBorr_history_userAct) == 0:
        print()
        print(f"Halo, {active_user['nama']}! Tidak ada gadget yang anda pinjam.")

    elif len(gadBorr_history_userAct) > 0:
        print("---------------------------------")
        for i in range(len(gadBorr_history_userAct)):
            nama_item = item_position(gadBorr_history_userAct[i]['id_gadget'])['nama']  # gadget[index]['nama']
            jml_pinjam = gadBorr_history_userAct[i]['jumlah']
            print(f"{i+1}. {nama_item} (x{jml_pinjam})")

        print("---------------------------------")
        nmr_pinjam = int(input("Masukkan nomor peminjaman: "))

        if 1 <= nmr_pinjam <= len(gadBorr_history_userAct):
            print("---------------------------------")
            print("*Format tanggal  -->  DD/MM/YYYY")
            tgl_balik = str(input("Tanggal pengembalian: "))
            
            if is_tanggalValid(tgl_balik):
        
                item_dict = gadBorr_history_userAct[nmr_pinjam-1]
                id_item = item_dict['id_gadget']
                line_item = item_position(id_item) # jadi gadget[index]
                idx_atBorr_history = gadgetBorr_history.index(item_dict)

                gadRet_temp = {}
                gadRet_temp['id'] = str(len(gadgetRet_history)+1)
                gadRet_temp['id_peminjaman'] = item_dict['id']
                gadRet_temp['tanggal_pengembalian'] = tgl_balik

                # menambah data pada array gadgetRet_history
                gadgetRet_history.append(gadRet_temp)
                # mengubah kembali data jumlah pada array gadgets
                line_item['jumlah'] += item_dict['jumlah']
                # mengubah data is_returned pada array gadgetBorr_history menjadi true
                gadgetBorr_history[idx_atBorr_history]['is_returned'] = 'true'
                
                print()
                print(f"Item {line_item['nama']} (x{item_dict['jumlah']}) telah dikembalikan.")
            else:
                print()
                print("Input data tanggal tidak valid!")

        elif nmr_pinjam < 1:
            print()
            print("Input nomor peminjaman tidak valid!")
        
        elif nmr_pinjam > len(gadBorr_history_userAct):
            print()
            print("Input nomor peminjaman diluar indeks!")

# F10 - Meminta Consumable
def minta_consumable():
    id_consumable = input('Masukan ID item: ').upper()
    qty = int(input('Jumlah: '))
    date = input('Tanggal Permintaan: ')

    if is_tanggalValid(date):
        
        if (qty <= 0) or (qty > 99999):
            print()
            print('Jumlah tidak valid!')
        
        else: 
            if len(cons) != 0 :
                i = 0
                for lines in cons:
                    i += 1
                    if (lines['id'] == id_consumable):
                        if (qty <= int(lines['jumlah'])):
                            lines['jumlah'] -=  qty
                            print()
                            print('Item '+str(lines['nama'])+' (x'+str(qty)+') telah berhasil diambil')
                            
                            new_history = {
                                'id': str(len(consumable_history) + 1),
                                'id_pengambil': active_user['id'],
                                'id_consumable': id_consumable,
                                'tanggal_pengambilan': date,
                                'jumlah': qty
                            }
                                
                            consumable_history.append(new_history)
                            break
                    
                        elif (qty > int(lines['jumlah'])):
                            print()
                            print('Jumlah barang tidak mencukupi.')
                            break
                    
                    elif (i == (len(cons))) and (lines['id'] != id_consumable):
                        print()
                        print('Tidak ada barang dengan ID '+ str(id_consumable)+'.')
                        break
                    
            else:
                print()
                print('Belum ada barang tersedia.')
            
    else:       
        print()
        print('Tanggal tidak valid!')

# F11 - Melihat Riwayat Peminjaman Gadget
def riwayat_pinjam():
    gadbor_temp = date_parser(gadgetBorr_history)
    array_sorted = [gadbor_temp[0]]
    for n in range(1, len(gadbor_temp)):
        sorting_date_gadBorr(array_sorted, n, gadgetBorr_history)
    balikin_tgl_gadBorr(array_sorted)
    # array gadget borrow sudah terurut mengecil berdasarkan tanggal

    i = len(gadgetBorr_history)
    
    if (i == 0):
        print('Data kosong.')

    else:
        if i>4:
            count = 0
            while count < i:
                if (i - count) > 5:
                    for k in range(count, count+5):
                        id_gadget = array_sorted[k]['id_gadget']
                        the_item = item_position(id_gadget)
                        nama_item = the_item['nama']
                        id_peminjam = array_sorted[k]['id_peminjam']
                        for line in user:
                            if id_peminjam == line['id']:
                                nama_peminjam = line['nama']

                        print('ID Peminjaman \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:', nama_peminjam) #harus ambil nama dari user.csv pake index id_peminjam
                        print('Nama Gadget \t\t:',nama_item)
                        print('Tanggal Peminjaman \t:',array_sorted[k]['tanggal_peminjaman'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()
    
                    extend = input('Extend list? \t(Y/N): ').upper()
                    print()
                    if extend == 'Y':
                        count += 5
                    elif extend == 'N':
                        count = i
                else:
                    for k in range(count, i):
                        id_gadget = array_sorted[k]['id_gadget']
                        the_item = item_position(id_gadget)
                        nama_item = the_item['nama']
                        id_peminjam = array_sorted[k]['id_peminjam']
                        for line in user:
                            if id_peminjam == line['id']:
                                nama_peminjam = line['nama']

                        print('ID Peminjaman \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:', nama_peminjam) #harus ambil nama dari user.csv pake index id_peminjam
                        print('Nama Gadget \t\t:',nama_item)
                        print('Tanggal Peminjaman \t:',array_sorted[k]['tanggal_peminjaman'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()
                    count += 5
        else:
            for k in range(0,i):
                id_gadget = array_sorted[k]['id_gadget']
                the_item = item_position(id_gadget)
                nama_item = the_item['nama']
                id_peminjam = array_sorted[k]['id_peminjam']
                for line in user:
                    if id_peminjam == line['id']:
                        nama_peminjam = line['nama']

                print('ID Peminjaman \t\t:',array_sorted[k]['id'])
                print('Nama Pengambil \t\t:',nama_peminjam) #harus ambil nama dari user.csv pake index id_peminjam
                print('Nama Gadget \t\t:',nama_item)
                print('Tanggal Peminjaman \t:',array_sorted[k]['tanggal_peminjaman'])
                print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                print()

# F12 - Melihat Riwayat Pengembalian Gadget
def riwayat_kembali(): 
    gadret_temp = date_parser(gadgetRet_history)
    array_sorted = [gadret_temp[0]]
    for n in range(1, len(gadret_temp)):
        sorting_date_gadRet(array_sorted, n, gadgetRet_history)
    balikin_tgl_gadRet(array_sorted)
    # array gadget return sudah terurut mengecil berdasarkan tanggal

    i = len(gadgetRet_history)
    
    if (i == 0):
        print('Data kosong.')

    else:
        if i>4:
            count = 0
            while count < i:
                if (i - count) > 5:
                    for k in range(count, count+5):
                        id_peminjaman = array_sorted[k]['id_peminjaman']
                        for lines in gadgetBorr_history:
                            if id_peminjaman == lines['id']:
                                id_item = lines['id_gadget']
                                the_item = item_position(id_item)
                                nama_item = the_item['nama']
                                break
                        for lines in gadgetBorr_history:
                            if id_peminjaman == lines['id']:
                                id_peminjam = lines['id_peminjam']
                                break
                        for lines in user:
                            if id_peminjam == lines['id']:
                                nama_peminjam = lines['nama']
                                break
            
                        print('ID Pengembalian \t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:',nama_peminjam)
                        print('Nama Gadget \t\t:',nama_item)
                        print('Tanggal Pengembalian \t:',array_sorted[k]['tanggal_pengembalian'])
                        print()

                    extend = input('Extend list? \t(Y/N): ').upper()
                    print()
                    if extend == 'Y':  
                        count += 5 
                    elif extend == 'N':
                        count = i
                else:
                    for k in range(count, i):
                        id_peminjaman = array_sorted[k]['id_peminjaman']
                        for lines in gadgetBorr_history:
                            if id_peminjaman == lines['id']:
                                id_item = lines['id_gadget']
                                the_item = item_position(id_item)
                                nama_item = the_item['nama']
                                break
                        for lines in gadgetBorr_history:
                            if id_peminjaman == lines['id']:
                                id_peminjam = lines['id_peminjam']
                                break
                        for lines in user:
                            if id_peminjam == lines['id']:
                                nama_peminjam = lines['nama']
                                break
            
                        print('ID Pengembalian \t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:',nama_peminjam)
                        print('Nama Gadget \t\t:',nama_item)
                        print('Tanggal Pengembalian \t:',array_sorted[k]['tanggal_pengembalian'])
                        print()
                    count += 5

        else:
            for k in range(0,i):
                id_peminjaman = array_sorted[k]['id_peminjaman']

                for lines in gadgetBorr_history:
                    if id_peminjaman == lines['id']:
                        id_item = lines['id_gadget']
                        the_item = item_position(id_item)
                        nama_item = the_item['nama']
                        break
                for lines in gadgetBorr_history:
                    if id_peminjaman == lines['id']:
                        id_peminjam = lines['id_peminjam']
                        break
                for lines in user:
                    if id_peminjam == lines['id']:
                        nama_peminjam = lines['nama']
                        break
                print('ID Pengembalian \t:',array_sorted[k]['id'])
                print('Nama Pengambil \t\t:', nama_peminjam)
                print('Nama Gadget \t\t:',nama_item)
                print('Tanggal Pengembalian \t:',array_sorted[k]['tanggal_pengembalian'])
                print()

# F13 - Melihat Riwayat Pengambilan Consumable
def riwayat_ambil():
    consHis_temp = date_parser(consumable_history)
    array_sorted = [consHis_temp[0]]
    for n in range(1, len(consHis_temp)):
        sorting_date_consHis(array_sorted, n, consumable_history)
    balikin_tgl_consHis(array_sorted)

    i = len(consumable_history)
    
    if (i == 0):
        print('Data kosong.')

    else:
        if i>4:
            count = 0
            while count < i:
                if (i - count) > 5:
                    for k in range(count, count+5):
                        id_consumable = array_sorted[k]['id_consumable']
                        the_item = item_position(id_consumable)
                        nama_item = the_item['nama']

                        id_pengambil = array_sorted[k]['id_pengambil']
                        for line in user:
                            if id_pengambil == line['id']:
                                nama_pengambil = line['nama']

                        print('ID Pengambilan \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:',nama_pengambil)
                        print('Nama Consumable \t:',nama_item)
                        print('Tanggal Pengambilan \t:',array_sorted[k]['tanggal_pengambilan'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()

                    extend = input('Extend list? \t(Y/N): ').upper()
                    print()
                    if extend == 'Y':
                        count += 5
                    elif extend == 'N':
                        count = i
                else:
                    for k in range(count, i):
                        id_consumable = array_sorted[k]['id_consumable']
                        the_item = item_position(id_consumable)
                        nama_item = the_item['nama']

                        id_pengambil = array_sorted[k]['id_pengambil']
                        for line in user:
                            if id_pengambil == line['id']:
                                nama_pengambil = line['nama']

                        print('ID Pengambilan \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:',nama_pengambil)
                        print('Nama Consumable \t:',nama_item)
                        print('Tanggal Pengambilan \t:',array_sorted[k]['tanggal_pengambilan'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()
                    count += 5

        else:
            for k in range(0,i):
                id_consumable = array_sorted[k]['id_consumable']
                the_item = item_position(id_consumable)
                nama_item = the_item['nama']

                id_pengambil = array_sorted[k]['id_pengambil']
                for line in user:
                    if id_pengambil == line['id']:
                        nama_pengambil = line['nama']
                
                print('ID Pengambilan \t\t:',array_sorted[k]['id'])
                print('Nama Pengambil \t\t:',nama_pengambil)
                print('Nama Consumable \t:',nama_item)
                print('Tanggal Pengambilan \t:',array_sorted[k]['tanggal_pengambilan'])
                print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                print()

# F14 - Load Data

## FUNGSI UNTUK LOAD BEBERAPA file.csv
# fs. utk load file user.csv
def load_user():
    global user_header
    global folder

    user = [] 
    f = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "user.csv","r")
    raw_lines = f.readlines()
    f.close()

    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    # data udah rapih

    raw_header = lines.pop(0)
    user_header = convertLine_to_arrDat(raw_header)

    for line in lines:
        user_Dict = {}
        raw_data = convertLine_to_arrDat(line)
        user_Dict['id'] = raw_data[0]
        user_Dict['username'] = raw_data[1]
        user_Dict['nama'] = raw_data[2]
        user_Dict['alamat'] = raw_data[3]
        user_Dict['pass'] = raw_data[4]
        user_Dict['role'] = raw_data[5].replace('\n', '')
        user.append(user_Dict)
    return user
# fs. utk load file gadget.csv
def load_gadgets():
    global gadget_header
    global folder

    gadgets = [] 
    f = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "gadget.csv","r")
    raw_lines = f.readlines()
    f.close()

    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    # data udah rapih

    raw_header = lines.pop(0)
    gadget_header = convertLine_to_arrDat(raw_header)

    for line in lines:
        gadget_Dict = {}
        raw_data = convertLine_to_arrDat(line)
        realValue_data = arr_to_realValues(raw_data)
        gadget_Dict['id'] = realValue_data[0]
        gadget_Dict['nama'] = realValue_data[1]
        gadget_Dict['deskripsi'] = realValue_data[2]
        gadget_Dict['jumlah'] = realValue_data[3]
        gadget_Dict['rarity'] = realValue_data[4]
        gadget_Dict['tahun_ditemukan'] = realValue_data[5].replace('\n', '')
        gadgets.append(gadget_Dict)
    return gadgets
# fs. utk load file consumable.csv
def load_consumables():
    global cons_header
    global folder

    consumables = [] 
    f = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "consumable.csv","r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    # data udah rapih

    raw_header = lines.pop(0)
    cons_header = convertLine_to_arrDat(raw_header)

    for line in lines:
        cons_Dict = {}
        raw_data = convertLine_to_arrDat(line)
        realValue_data = arr_to_realValues(raw_data)
        cons_Dict['id'] = realValue_data[0]
        cons_Dict['nama'] = realValue_data[1]
        cons_Dict['deskripsi'] = realValue_data[2]
        cons_Dict['jumlah'] = realValue_data[3]
        cons_Dict['rarity'] = realValue_data[4].replace('\n', '')
        consumables.append(cons_Dict)
    return consumables
# fs. utk load file gadget_borrow_history.csv
def load_gadBorrow_history():
    global gadgetBorr_header
    global folder

    gadgetBorr_history = []
    f = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "gadget_borrow_history.csv","r")
    raw_lines = f.readlines()
    f.close()
    
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    # data udah rapih

    raw_header = lines.pop(0)
    gadgetBorr_header = convertLine_to_arrDat(raw_header)

    for line in lines:
        gadgetBorr_Dict = {}
        raw_data = convertLine_to_arrDat(line)
        gadgetBorr_Dict['id'] = raw_data[0]
        gadgetBorr_Dict['id_peminjam'] = raw_data[1]
        gadgetBorr_Dict['id_gadget'] = raw_data[2]
        gadgetBorr_Dict['tanggal_peminjaman'] = raw_data[3]
        gadgetBorr_Dict['jumlah'] = raw_data[4]
        gadgetBorr_Dict['is_returned'] = raw_data[5].replace('\n', '')
        # turn to real value
        gadgetBorr_Dict['jumlah'] = int(gadgetBorr_Dict['jumlah'])
        gadgetBorr_history.append(gadgetBorr_Dict)
    return gadgetBorr_history
# fs. utk load file gadget_return_history.csv
def load_gadReturn_history():
    global gadgetRet_header
    global folder

    gadgetRet_history = []
    f = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "gadget_return_history.csv","r")
    raw_lines = f.readlines()
    f.close()

    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    # data udah rapih

    raw_header = lines.pop(0)
    gadgetRet_header = convertLine_to_arrDat(raw_header)

    for line in lines:
        gadgetRet_Dict = {}
        raw_data = convertLine_to_arrDat(line)
        gadgetRet_Dict['id'] = raw_data[0]
        gadgetRet_Dict['id_peminjaman'] = raw_data[1]
        gadgetRet_Dict['tanggal_pengembalian'] = raw_data[2].replace('\n', '')

        gadgetRet_history.append(gadgetRet_Dict)
    return gadgetRet_history
# fs. utk load file consumable_history.csv
def load_consumable_history():
    global consHistory_header
    global folder

    consumable_history = []
    f = open(os.path.abspath(os.getcwd()) + "\\" + folder + "\\" + "consumable_history.csv","r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    # data udah rapih

    raw_header = lines.pop(0)
    consHistory_header = convertLine_to_arrDat(raw_header)

    for line in lines:
        consHistory_Dict = {}
        raw_data = convertLine_to_arrDat(line)
        consHistory_Dict['id'] = raw_data[0]
        consHistory_Dict['id_pengambil'] = raw_data[1]
        consHistory_Dict['id_consumable'] = raw_data[2]
        consHistory_Dict['tanggal_pengambilan'] = raw_data[3]
        consHistory_Dict['jumlah'] = raw_data[4].replace('\n', '')
        # turn to real value
        consHistory_Dict['jumlah'] = int(consHistory_Dict['jumlah'])
        consumable_history.append(consHistory_Dict)
    return consumable_history

# F15 - Save Date
def save():
    foldername = input('Masukkan nama folder: ')
    saveloc = os.path.join(os.path.abspath(os.getcwd()), foldername)

    try: 
        os.makedirs(saveloc) #Cek apakah sudah ada directory dengan nama yang sama, jika belum akan dibuat.
    except: 
        None

    datas_as_string_user = convertDatas_to_string(user_header, user)
    datas_as_string_gadget = convertDatas_to_string(gadget_header, gadgets)
    datas_as_string_consumable = convertDatas_to_string(cons_header, cons)
    datas_as_string_gadget_borrow_history = convertDatas_to_string(gadgetBorr_header, gadgetBorr_history)
    datas_as_string_gadget_return_history = convertDatas_to_string(gadgetRet_header, gadgetRet_history)
    datas_as_string_consumable_history = convertDatas_to_string(consHistory_header, consumable_history)

    f1 = open(os.path.abspath(os.getcwd()) + "\\" + foldername + "\\" + "user.csv", "w")
    f1.write(datas_as_string_user)
    f1.close()

    f2 = open(os.path.abspath(os.getcwd()) + "\\" + foldername + "\\" + "gadget.csv", "w")
    f2.write(datas_as_string_gadget)
    f2.close()

    f3 = open(os.path.abspath(os.getcwd()) + "\\" + foldername + "\\" + "consumable.csv", "w")
    f3.write(datas_as_string_consumable)
    f3.close()

    f4 = open(os.path.abspath(os.getcwd()) + "\\" + foldername + "\\" + "gadget_borrow_history.csv", "w")
    f4.write(datas_as_string_gadget_borrow_history)
    f4.close()

    f5 = open(os.path.abspath(os.getcwd()) + "\\" + foldername + "\\" + "gadget_return_history.csv", "w")
    f5.write(datas_as_string_gadget_return_history)
    f5.close()

    f6 = open(os.path.abspath(os.getcwd()) + "\\" + foldername + "\\" + "consumable_history.csv", "w")
    f6.write(datas_as_string_consumable_history)
    f6.close()

    print()
    print("Data telah berhasil disimpan.")

# F16 - Help
def help(role):
    if role == 'admin':
        print ('''
        ======================================== Help =========================================
        register       - Untuk melakukan registrasi user baru.
        carirarity     - Untuk mencari gadget dengan rarity tertentu.
        caritahun      - Untuk mencari gadget berdasarkan tahun yang ditemukan.
        tambahitem     - Untuk melakukan penambahan item.
        hapusitem      - Untuk menghapus item dari database.
        ubahjumlah     - Untuk mengubah jumlah gadget dan consumable yang terdapat dalam sistem.
        riwayatpinjam  - Untuk melihat riwayat peminjaman Gadget.
        riwayatkembali - Untuk melihat riwayat pengembalian Gadget.
        riwayatambil   - Untuk melihat riwayat pengambilan consumables.
        save           - Untuk melakukan penyimpanan data ke file setelah melakukan perubahan
        help           - Untuk memberikan panduan penggunaan sistem.
        exit           - Untuk keluar dari aplikasi.
        =======================================================================================
        ''')
    elif role == 'user':
        print ('''
        ======================================== Help =========================================
        carirarity     - Untuk mencari gadget dengan rarity tertentu.
        caritahun      - Untuk mencari gadget berdasarkan tahun yang ditemukan.
        pinjam         - Untuk melakukan peminjaman Gadget.
        kembalikan     - Untuk mengembalikan Gadget.
        minta          - Untuk meminta Consumable.
        save           - Untuk melakukan penyimpanan data ke file setelah melakukan perubahan
        help           - Untuk memberikan panduan penggunaan sistem.
        exit           - Untuk keluar dari aplikasi.
        =======================================================================================
        ''')

# F17 - Exit
def exit():
    print()
    jawab = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (Y/N): ")

    if jawab == 'y' or jawab == 'Y':
        save()
    else:
        print()
        print("Data tidak jadi disimpan.")
        pass

# active_user merupakan dictionary kosong jika belum ada login yang valid
active_user = {}    

parser = argparse.ArgumentParser(description='Load Data')
parser.add_argument('namaFolder')
args = parser.parse_args()
print("==============================================")
print("                 LOADING DATA                 ")
print("==============================================")
print("Sabar! Lagi loading...")
print()
folder = args.namaFolder

# loading data user dengan mengisi suatu variable
user_header = []
user = load_user()
# loading data gadget dengan mengisi suatu variable
gadget_header = []
gadgets = load_gadgets()
# loading data consumable dengan mengisi suatu variable
cons_header = []
cons = load_consumables()
# loading data gadget_borrow_history dengan mengisi suatu variable
gadgetBorr_header = []
gadgetBorr_history = load_gadBorrow_history()
# loading data gadget_return_history dengan mengisi suatu variable
gadgetRet_header = []
gadgetRet_history = load_gadReturn_history()
# loading data consumable_history dengan mengisi suatu variable
consHistory_header = []
consumable_history = load_consumable_history()

isRun = True    # boolean untuk menjalankan main program
login()         # bila berhasil login, dict. active_user akan terisi dengan akun yang sedang aktif

# main program
while (isRun):
    print("========================== PILIH MENU ===========================")
    print("Masukkan menu yang ingin dipilih (ketik 'help' untuk info menu).")
    print("=================================================================")
    menu_chosen = input(">>> ")
    if active_user['role'] == 'admin':
        if menu_chosen == 'register':
            reg()
            print()
        elif menu_chosen == 'carirarity':
            carirarity()
        elif menu_chosen == 'caritahun':
            caritahun()
        elif menu_chosen == 'tambahitem':
            tambahitem()
            print()
        elif menu_chosen == 'hapusitem':
            delete_item()
            print()
        elif menu_chosen == 'ubahjumlah':
            ubah_jumlah()
            print()
        elif menu_chosen == 'pinjam':
            print()
            print("Akses hanya diberikan untuk User. ")
            print()
        elif menu_chosen == 'kembalikan':
            print()
            print("Akses hanya diberikan untuk User. ")
            print()
        elif menu_chosen == 'minta':
            print()
            print("Akses hanya diberikan untuk User. ")
            print()
        elif menu_chosen == 'riwayatpinjam':
            print()
            riwayat_pinjam()
        elif menu_chosen == 'riwayatkembali':
            print()
            riwayat_kembali()
        elif menu_chosen == 'riwayatambil':
            print()
            riwayat_ambil()
        elif menu_chosen == 'save':
            save()
            print()
        elif menu_chosen == 'help':
            help(active_user['role'])
        elif menu_chosen == 'exit':
            exit()
            print("-------------------------------")
            print("(^///^) Selamat Jalan! (^///^)")
            print("-------------------------------")
            isRun = False
        else:
            print()
            print("Menu tidak tersedia.")
            print()

    elif active_user['role'] == 'user':
        if menu_chosen == 'register':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'carirarity':
            carirarity()
        elif menu_chosen == 'caritahun':
            caritahun()
        elif menu_chosen == 'tambahitem':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'hapusitem':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'ubahjumlah':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'pinjam':
            pinjam_gadget()
            print()
        elif menu_chosen == 'kembalikan':
            balikin_gadget()
            print()
        elif menu_chosen == 'minta':
            minta_consumable()
            print()
        elif menu_chosen == 'riwayatpinjam':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'riwayatkembali':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'riwayatambil':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'save':
            save()
            print()
        elif menu_chosen == 'help':
            help(active_user['role'])
        elif menu_chosen == 'exit':
            exit()
            print("-------------------------------")
            print("(^///^) Selamat Jalan! (^///^)")
            print("-------------------------------")
            isRun = False
        else:
            print()
            print("Menu tidak tersedia.")
            print()