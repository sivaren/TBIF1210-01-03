'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# F13 - Melihat Riwayat Pengambilan Consumable
def riwayat_ambil():
    consHis_temp = date_parser(consumable_history)
    array_sorted = [consHis_temp[0]]
    for n in range(1, len(consHis_temp)):
        sorting_date_consHis(array_sorted, n, consumable_history)
    balikin_tgl_consHis(array_sorted)

    i = len(consumable_history)
    
    if (i == 0):
        print('Data kosong.')

    else:
        if i>4:
            count = 0
            while count < i:
                if (i - count) > 5:
                    for k in range(count, count+5):
                        id_consumable = array_sorted[k]['id_consumable']
                        the_item = item_position(id_consumable)
                        nama_item = the_item['nama']

                        id_pengambil = array_sorted[k]['id_pengambil']
                        for line in user:
                            if id_pengambil == line['id']:
                                nama_pengambil = line['nama']

                        print('ID Pengambilan \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:',nama_pengambil)
                        print('Nama Consumable \t:',nama_item)
                        print('Tanggal Pengambilan \t:',array_sorted[k]['tanggal_pengambilan'])
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
                        id_consumable = array_sorted[k]['id_consumable']
                        the_item = item_position(id_consumable)
                        nama_item = the_item['nama']

                        id_pengambil = array_sorted[k]['id_pengambil']
                        for line in user:
                            if id_pengambil == line['id']:
                                nama_pengambil = line['nama']

                        print('ID Pengambilan \t\t:',array_sorted[k]['id'])
                        print('Nama Pengambil \t\t:',nama_pengambil)
                        print('Nama Consumable \t:',nama_item)
                        print('Tanggal Pengambilan \t:',array_sorted[k]['tanggal_pengambilan'])
                        print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                        print()
                    count += 5

        else:
            for k in range(0,i):
                id_consumable = array_sorted[k]['id_consumable']
                the_item = item_position(id_consumable)
                nama_item = the_item['nama']

                id_pengambil = array_sorted[k]['id_pengambil']
                for line in user:
                    if id_pengambil == line['id']:
                        nama_pengambil = line['nama']
                
                print('ID Pengambilan \t\t:',array_sorted[k]['id'])
                print('Nama Pengambil \t\t:',nama_pengambil)
                print('Nama Consumable \t:',nama_item)
                print('Tanggal Pengambilan \t:',array_sorted[k]['tanggal_pengambilan'])
                print('Jumlah \t\t\t:',array_sorted[k]['jumlah'])
                print()
