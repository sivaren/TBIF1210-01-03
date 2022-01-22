'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
