def menu():
    while True:
        print('Menu:')
        print('1. Cek Angka')
        print('2. Luas Segitiga')
        print('3. Keluar')
        pilihan = input('Pilih opsi: ')
        if pilihan == '1':
            cek_angka()
        elif pilihan == '2':
            luas()
        elif pilihan == '3':
            print('Terima kasih!')
            break
        else:
            print('Opsi tidak valid.')

def cek_angka():
    while True:
        angka = int(input('Masukkan angka: '))
        if angka == 0:
            print('Nol')
        elif angka % 2 == 0:
            print('Genap')
        else:
            print('Ganjil')
        if input('Apakah ingin melanjutkan? (y/n): ').lower() != 'y':
            break

def luas():
    while True:
        alas = float(input('Masukkan alas: '))
        tinggi = float(input('Masukkan tinggi: '))
        luas = 0.5 * alas * tinggi
        print(f'Luas segitiga: {luas}')
        if input('Apakah ingin melanjutkan? (y/n): ').lower() != 'y':
            break
        
if __name__ == '__main__':
    menu()






