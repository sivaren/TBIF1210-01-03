'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
