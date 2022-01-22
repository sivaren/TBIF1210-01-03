'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

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
