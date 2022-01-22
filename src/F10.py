'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# F10 - Meminta Consumable
def minta_consumable():
    id_consumable = input('Masukan ID item: ').upper()
    qty = int(input('Jumlah: '))
    date = input('Tanggal Permintaan: ')

    if is_tanggalValid(date):
        
        if (qty <= 0) or (qty > 99999):
            print()
            print('Jumlah tidak valid!')
        
        else: 
            if len(cons) != 0 :
                i = 0
                for lines in cons:
                    i += 1
                    if (lines['id'] == id_consumable):
                        if (qty <= int(lines['jumlah'])):
                            lines['jumlah'] -=  qty
                            print()
                            print('Item '+str(lines['nama'])+' (x'+str(qty)+') telah berhasil diambil')
                            
                            new_history = {
                                'id': str(len(consumable_history) + 1),
                                'id_pengambil': active_user['id'],
                                'id_consumable': id_consumable,
                                'tanggal_pengambilan': date,
                                'jumlah': qty
                            }
                                
                            consumable_history.append(new_history)
                            break
                    
                        elif (qty > int(lines['jumlah'])):
                            print()
                            print('Jumlah barang tidak mencukupi.')
                            break
                    
                    elif (i == (len(cons))) and (lines['id'] != id_consumable):
                        print()
                        print('Tidak ada barang dengan ID '+ str(id_consumable)+'.')
                        break
                    
            else:
                print()
                print('Belum ada barang tersedia.')
            
    else:       
        print()
        print('Tanggal tidak valid!')
