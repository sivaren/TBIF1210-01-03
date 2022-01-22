'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''
import os
import argparse

# F15 - Save
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
