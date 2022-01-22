'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''
import os
import argparse

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

parser = argparse.ArgumentParser(description='Load Data')
parser.add_argument('namaFolder')
args = parser.parse_args()
print("==============================================")
print("                 LOADING DATA                 ")
print("==============================================")
print("Sabar! Lagi loading...")
print()
folder = args.namaFolder