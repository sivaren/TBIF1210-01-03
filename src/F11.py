'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# F11 - Melihat Riwayat Peminjaman Gadget
def riwayat_pinjam():
    gadbor_temp = date_parser(gadgetBorr_history)
    array_sorted = [gadbor_temp[0]]
    for n in range(1, len(gadbor_temp)):
        sorting_date_gadBorr(array_sorted, n, gadgetBorr_history)
    balikin_tgl_gadBorr(array_sorted)
    # array gadget borrow sudah terurut mengecil berdasarkan tanggal

    i = len(gadgetBorr_history)
    
    if (i == 0):
        print('Data kosong.')

    else:
        if i>4:
            count = 0
            while count < i:
                if (i - count) > 5:
                    for k in range(count, count+5):
                        id_gadget = array_sorted[k]['id_gadget']
                        the_item = item_position(id_gadget)
                        nama_item = the_item['nama']
                        id_peminjam = array_sorted[k]['id_peminjam']
                        for line in user:
                            if id_peminjam == line['id']:
                                nama_peminjam = line['nama']

                        print('ID Peminjaman \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:', nama_peminjam) #harus ambil nama dari user.csv pake index id_peminjam
                        print('Nama Gadget \t\t:',nama_item)
                        print('Tanggal Peminjaman \t:',array_sorted[k]['tanggal_peminjaman'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()
    
                    extend = input('Extend list? \t(Y/N): ').upper()
                    print()
                    if extend == 'Y':
                        count += 5
                    elif extend == 'N':
                        count = i
                else:
                    for k in range(count, i):
                        id_gadget = array_sorted[k]['id_gadget']
                        the_item = item_position(id_gadget)
                        nama_item = the_item['nama']
                        id_peminjam = array_sorted[k]['id_peminjam']
                        for line in user:
                            if id_peminjam == line['id']:
                                nama_peminjam = line['nama']

                        print('ID Peminjaman \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:', nama_peminjam) #harus ambil nama dari user.csv pake index id_peminjam
                        print('Nama Gadget \t\t:',nama_item)
                        print('Tanggal Peminjaman \t:',array_sorted[k]['tanggal_peminjaman'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()
                    count += 5
        else:
            for k in range(0,i):
                id_gadget = array_sorted[k]['id_gadget']
                the_item = item_position(id_gadget)
                nama_item = the_item['nama']
                id_peminjam = array_sorted[k]['id_peminjam']
                for line in user:
                    if id_peminjam == line['id']:
                        nama_peminjam = line['nama']

                print('ID Peminjaman \t\t:',array_sorted[k]['id'])
                print('Nama Pengambil \t\t:',nama_peminjam) #harus ambil nama dari user.csv pake index id_peminjam
                print('Nama Gadget \t\t:',nama_item)
                print('Tanggal Peminjaman \t:',array_sorted[k]['tanggal_peminjaman'])
                print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                print()
