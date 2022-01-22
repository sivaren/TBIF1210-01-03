'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
