'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
