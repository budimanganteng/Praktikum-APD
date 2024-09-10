
print("Selamat Datang Di gudang part Komputer")
print("Silahkan Registrasi terlebih dahulu")
data_akun = []
data_password = []
tanya = "iya"
while tanya == "iya" :
    a = input("Daftarkan Username anda : ")
    b = input("Daftarkan Password Anda : ")
    data_akun.append(a)
    data_password.append(b)
    print(data_akun,data_password)
    print('')
    c = False
    while c == False :
        tanya =  input("Daftarkan akun lagi (iya/tidak)? ")
        c = tanya == "iya" or tanya == "tidak"
        break
#Login
d = False
while d == False :
    s = input("Masukkan Username anda : ")
    d = s in data_akun
    if d == True:
        j = data_akun.index(s)
        r = False
        while r == False:
            p = input ("Masukkan Password anda : ")
            r = p == data_password[j]
            if r == True:
                break
            else:print("Password anda salah ")
    else:print("Mohon Maaf Username tidak terdaftar")
print("Login Berhasil")
print()

#Masuk Program
print("============================================")
part_komputer = [{"Paket A" : "ak"}]


#Perulangan pada crud
while True:
    try:
        print("1. Tampilkan data Part Komputer")
        print("2. Tambahkan data Part Komputer")
        print("3. Ubah data Part Komputer     ")
        print("4. Hapus data Part Komputer    ")
        print("====================================")
        pilih_menu = input("Masukkan pilihan Anda: ")

        # Tampilkan data
        if pilih_menu == "1":
            for key, Value in part_komputer.items():
                print(f"{key}, {Value}")
            # for b, m in part_komputer.items():
            #     print(f'Part Komputer : {b} : "Merek Part Komputer :" {m}')

        # Tambahkan data
        elif pilih_menu == "2":
            m = str(input("Masukkan Merek Part Komputer yang mau anda Tambah : "))
            b = str(input("Masukkan Part Komputer yang ingin anda Tambah : "))
            part_komputer.update({m : b})
            print("part komputer baru '{}' telah ditambahkan.".format(m))

        # Ubah data
        elif pilih_menu == "3":
            d = str(input("Masukkan part komputer : "))
            c = str(input("Masukkan Merek Yang baru : "))
            part_komputer[d]=c

        # Hapus data
        elif pilih_menu == "4":
                d = str(input("masukan key yang ingin di hapus: "))
                cache = part_komputer.pop(d)

        else:print("Pilihan Anda Tidak Valid")
        
    except ValueError :
        print("tidak valid")

