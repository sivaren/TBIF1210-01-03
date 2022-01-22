'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
