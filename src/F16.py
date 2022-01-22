'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# F16 - Help
def help(role):
    if role == 'admin':
        print ('''
        ======================================== Help =========================================
        register       - Untuk melakukan registrasi user baru.
        carirarity     - Untuk mencari gadget dengan rarity tertentu.
        caritahun      - Untuk mencari gadget berdasarkan tahun yang ditemukan.
        tambahitem     - Untuk melakukan penambahan item.
        hapusitem      - Untuk menghapus item dari database.
        ubahjumlah     - Untuk mengubah jumlah gadget dan consumable yang terdapat dalam sistem.
        riwayatpinjam  - Untuk melihat riwayat peminjaman Gadget.
        riwayatkembali - Untuk melihat riwayat pengembalian Gadget.
        riwayatambil   - Untuk melihat riwayat pengambilan consumables.
        save           - Untuk melakukan penyimpanan data ke file setelah melakukan perubahan
        help           - Untuk memberikan panduan penggunaan sistem.
        exit           - Untuk keluar dari aplikasi.
        =======================================================================================
        ''')
    elif role == 'user':
        print ('''
        ======================================== Help =========================================
        carirarity     - Untuk mencari gadget dengan rarity tertentu.
        caritahun      - Untuk mencari gadget berdasarkan tahun yang ditemukan.
        pinjam         - Untuk melakukan peminjaman Gadget.
        kembalikan     - Untuk mengembalikan Gadget.
        minta          - Untuk meminta Consumable.
        save           - Untuk melakukan penyimpanan data ke file setelah melakukan perubahan
        help           - Untuk memberikan panduan penggunaan sistem.
        exit           - Untuk keluar dari aplikasi.
        =======================================================================================
        ''')

'''
register - admin
login - admin, user
carirarity - admin, user
caritahun - admin, user
tambahitem - admin
hapusitem - admin
ubahjumlah - admin
pinjam - user
kembalikan - user
minta - user
riwayatpinjam - admin
riwayatkembali - admin
riwayatambil - admin
save - admin, user
help - admin, user
exit - admin, user

admin = register, login carirarity caritahun tambahitem hapusitem ubahjumlah riwayatpinjam riwayatkembali riwayatambil save help exit
user = login carirarity caritahun pinjam kembalikan minta save help exit
'''
