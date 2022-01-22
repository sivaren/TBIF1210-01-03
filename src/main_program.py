'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# main program
while (isRun):
    print("========================== PILIH MENU ===========================")
    print("Masukkan menu yang ingin dipilih (ketik 'help' untuk info menu).")
    print("=================================================================")
    menu_chosen = input(">>> ")
    if active_user['role'] == 'admin':
        if menu_chosen == 'register':
            reg()
            print()
        elif menu_chosen == 'carirarity':
            carirarity()
        elif menu_chosen == 'caritahun':
            caritahun()
        elif menu_chosen == 'tambahitem':
            tambahitem()
            print()
        elif menu_chosen == 'hapusitem':
            delete_item()
            print()
        elif menu_chosen == 'ubahjumlah':
            ubah_jumlah()
            print()
        elif menu_chosen == 'pinjam':
            print()
            print("Akses hanya diberikan untuk User. ")
            print()
        elif menu_chosen == 'kembalikan':
            print()
            print("Akses hanya diberikan untuk User. ")
            print()
        elif menu_chosen == 'minta':
            print()
            print("Akses hanya diberikan untuk User. ")
            print()
        elif menu_chosen == 'riwayatpinjam':
            print()
            riwayat_pinjam()
        elif menu_chosen == 'riwayatkembali':
            print()
            riwayat_kembali()
        elif menu_chosen == 'riwayatambil':
            print()
            riwayat_ambil()
        elif menu_chosen == 'save':
            save()
            print()
        elif menu_chosen == 'help':
            help(active_user['role'])
        elif menu_chosen == 'exit':
            exit()
            print("-------------------------------")
            print("(^///^) Selamat Jalan! (^///^)")
            print("-------------------------------")
            isRun = False
        else:
            print()
            print("Menu tidak tersedia.")
            print()

    elif active_user['role'] == 'user':
        if menu_chosen == 'register':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'carirarity':
            carirarity()
        elif menu_chosen == 'caritahun':
            caritahun()
        elif menu_chosen == 'tambahitem':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'hapusitem':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'ubahjumlah':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'pinjam':
            pinjam_gadget()
            print()
        elif menu_chosen == 'kembalikan':
            balikin_gadget()
            print()
        elif menu_chosen == 'minta':
            minta_consumable()
            print()
        elif menu_chosen == 'riwayatpinjam':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'riwayatkembali':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'riwayatambil':
            print()
            print("Akses hanya diberikan untuk Admin. ")
            print()
        elif menu_chosen == 'save':
            save()
            print()
        elif menu_chosen == 'help':
            help(active_user['role'])
        elif menu_chosen == 'exit':
            exit()
            print("-------------------------------")
            print("(^///^) Selamat Jalan! (^///^)")
            print("-------------------------------")
            isRun = False
        else:
            print()
            print("Menu tidak tersedia.")
            print()