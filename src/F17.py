'''
File ini hanya untuk maintenance,
    tidak dipergunakan untuk di-run.
'''

# F17 - Exit
def exit():
    print()
    jawab = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (Y/N): ")

    if jawab == 'y' or jawab == 'Y':
        save()
    else:
        print()
        print("Data tidak jadi disimpan.")
        pass
