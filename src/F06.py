'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
