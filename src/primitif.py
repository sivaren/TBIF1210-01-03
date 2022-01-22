'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
