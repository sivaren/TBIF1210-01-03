'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
def ubah_jumlah():
    id_item = input("Masukkan ID item: ")

    if isID_Valid(id_item):
        if item_existence(id_item):
            change_qty = int(input("Masukkan jumlah: "))
            taken_from = which_item(id_item)
            the_item = item_position(id_item)
            item_idx = taken_from.index(the_item)

            the_qty = int(the_item['jumlah'])
            now_qty = the_qty + change_qty

            if now_qty < 0 :
                print()
                print(f"{abs(change_qty)} {the_item['nama']} gagal dibuang karena stok kurang. Stok sekarang: {the_qty} (< {abs(change_qty)})")
            else:
                taken_from[item_idx]['jumlah'] = now_qty

                if now_qty > the_qty:
                    print()
                    print(f"{change_qty} {the_item['nama']} berhasil ditambah. Stok sekarang: {now_qty}")
                elif now_qty < the_qty:
                    print()
                    print(f"{abs(change_qty)} {the_item['nama']} berhasil dibuang. Stok sekarang: {now_qty}")
                else:
                    print()
                    print(f"Jumlah {the_item['nama']} tetap sama. Stok sekarang: {now_qty}")
        else:
            print()
            print("Tidak ada item dengan ID tersebut.")
    else:
        print()
        print("Input ID item tidak valid!")
