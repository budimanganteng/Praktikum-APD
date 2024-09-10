import os #ini sebagai untuk bersihkan terminal
import pyfiglet #untuk Sebagai logo sound
import pwinput #Untuk mensensor katasandi
os.system('pip install pyfiglet')#install pyfiglet
os.system('pip install pwinput')#install pwinput
import time #untuk mengatur jeda waktu program
class color: #untuk warna
		g = '\033[92m' #warna green
		y = '\033[93m' #warna Yellow
		r = '\033[91m' #Warna Red
		w = '\033[0m'  #Warna White
		b = '\033[34m' #Warna Blue

def grafiti(): #Fungsi untuk gambar sound system
	print(color.g+(f"""
					  
░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░	 ██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗	██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║	╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║	░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝	██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░	╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝"""+color.g))
		

tuple = (['admin','admin']) #Username dan Password Admin menggunakan tuple
user = {} #database untuk user
paket_nomor = {} #database paket nomor
paket_alat = { # data base Utama
	1: {
		"Nama Paket": "Paket A",
		"Alat": ["1 unit mixer", "2 unit power ST-PA 300 watt", 
				 "2 unit mic Wireless","2 unit speaker gantung", 
				 "2 unit speaker beta tree", "1 Equalizer"],
		"Pesanan" : []
	},
	2: {
		"Nama Paket": "Paket B",
		"Alat": ["1 unit mixer", "1 Unit Speaker bass", 
				 "1 Unit speaker middle", "1 unit speaker beta tree", 
				 "1 unit speaker high", "2 unit power ST-PA 300 watt", 
				 "1 unit Equalizer", "1 unit Alesis"],
		"Pesanan" : []
	},
	3: {
		"Nama Paket": "Paket C",
		"Alat": ["1 unit mixer", "1 unit Equalizer", 
				 "2 unit speaker bass", "2 unit speaker gantung", 
				 "2 unit speaker middel", "1 unit speaker high", 
				 "2 unit power ST-PA 300 watt", "2 unit mic wireless", 
				 "2 unit beta tree"],
		"Pesanan" : []
	}
}


# fungsi untuk Memberisihkan Terminal
os.system("cls")

# fungsi pembatas untuk pyfiglet
def pembatas():
	print("="*70)

# fungsi untuk pyfiglet
def logo_sound():
	print("\n")
	pembatas()
	z = pyfiglet.figlet_format("SOUND SYSTEM") #Bentuk pyfiglet
	print(z)
	pembatas() 

#Fungsi Register
def registrasi():
	print("============================ Silahkan Registrasi ============================")
	username = input("Silahkan Daftarkan Username Anda: ")
	password = pwinput.pwinput(color.g + "Masukkan password: " + color.y)
	if len(password)<8:#Periksa panjang password dengan ketentuan < dari 8
		print("Password Anda Kurang dari 8")
		print(color.g+"\nTekan [Enter Untuk Registrasi Ulang]")
		input()
		os.system("cls")
		grafiti()
		time.sleep(1)
		registrasi()
	if username in user: #kondisi username Jika ada yang sudah digunakan
		print("Username Sudah Digunakan")
		print(color.g+"\nTEKAN [ENTER] KEMBALI KE MENU UTAMA...........")
		input()
		os.system("cls")
		grafiti()
		time.sleep(1)
		main_menu()
	elif username in tuple: #kondisi salah jika login menggunakan username dan password admin
		print(color.r+"Username Sudah Digunakan"+color.r)
		print(color.b+"\nTekan [Enter Untuk Registrasi Ulang]"+color.b)
		input()
		os.system("cls")
		grafiti()
		time.sleep(1)
		os.system("cls")
		main_menu()
	else:
		user[username]=password # kondisi untuk menambahkan username(catatan:di sini menggunakan dictionary)
		print("Registrasi Berhasil")
		print(color.g+"\nTekan [ENTER] Untuk Lanjut Ke Menu")
		input()
		os.system("cls")
		time.sleep(1)
		main_menu()

# Fungsi Login admin
def login_admin():
	os.system("cls")
	while True:
		logo_sound()
		username = input("Masukkan Username Admin: ")
		password = pwinput.pwinput(color.g + "Masukkan password: " + color.y)
		os.system("cls")
		print(color.b+"Memeriksa Data Input.......")
		time.sleep(3)
		if username == tuple[0] and password == tuple[1]: #kondisi untuk login sebagai admin dengan ketentuan indeks pada tuple
			print(color.r+"Login Ke Menu Admin")
			os.system("cls")
			time.sleep(1)
			menu_admin()

		else: #kondisi salah jika di luar indeks tuple
			print("Username dan Password Tidak Sesuai")
			print(color.r+"\nTekan [ENTER] untuk kembali ke menu")
			input()
			os.system("cls")
			time.sleep(1)
			main_menu()

#Fungsi Login User
def login_user():
	os.system("CLS")
	logo_sound()
	username = input("Masukkan Yang Sudah Di registrasi: ")
	password = pwinput.pwinput(color.g + "Masukkan password: " + color.y)
	if username in user and user[username] == password: #kondisi untuk mengecek apakah password username sudah sesuai dengan username yang di daftarkan oleh user
		print("Login Sebagai User Berhasil\n")
		print(color.g+"\nTekan [ENTER] Untuk Lanjut Ke Menu")
		input()
		os.system("cls")
		pembatas()
		os.system("cls")
		time.sleep(1)
		menu_user()
	else: #kondisi ketika password atau username yang sudah di daftarkan oleh user tidak sesuai
		print(color.r+"Username dan Password Tidak Cocok"+color.r)
		print(color.r+"\nTekan [ENTER] untuk kembali ke menu"+color.r)
		input()
		os.system("cls")
		time.sleep(1)
		main_menu()	
		
# Fungsi Melihat data Alat
def lihat_data_alat():
	logo_sound()
	os.system("cls")
	time.sleep(2)
	print("============================ Daftar Paket Pemesanan Alat Sound System ============================")
	print("=" * 40)
	for nomor_paket, paket_info in paket_alat.items(): #perulangan yang digunakan untuk melakukan perulangan melalui setiap elemen (item) yang ada dalam dictionary paket_alat.
		print(color.b+(f"No. Paket: {nomor_paket}"+color.b)) #Menampilkan Nomor Paket Alatnya
		print(color.b+(f"Nama Paket: {paket_info['Nama Paket']}"+color.b)) #Menampilkan Informasi Paket Apa saja yang ada di dictionary
		print("Alat:")
		for alat in paket_info['Alat']:#perulangan yang digunakan untuk melakukan perulangan setiap elemen yang ada dalam list 'Alat' ke dalam dictionary paket info dengan indeks alat
			print(f"- {alat}")#Menampilkan alat isi dari Paket di atas
		print("=" * 40)

# Fungsi Melihat Pesanan User
def lihat_data_pemesanan_user():
	os.system("cls")
	logo_sound()
	time.sleep(2)
	print("Daftar Pesanan Alat Sound System")
	print("=" * 40)
	for nomor_paket, paket_info in paket_alat.items():#perulangan yang digunakan untuk melakukan perulangan melalui setiap elemen (item) yang ada dalam dictionary paket_alat.
		print(f"No. Paket: {nomor_paket}") #Menampilkan nomor antrian user
		print(f"Nama Paket: {paket_info['Nama Paket']}") #Menampilkan 
		print("Pesanan:")
		for pesanan in paket_info['Pesanan']:#perulangan yang di gunakan untuk melakukan perulangan di setiap elemen yang ada di dalam 'pesanan' ke dalam dictionary
			print("")
			print(f"- Nomor Pesanan: {pesanan['Nomor Pesanan']}, Nama Pemesan: {pesanan['Nama Pemesan']}") #menampilkan nomor pesanan, nama pemesannya
		print("=" * 40)


# Fungsi Menambahkan Paketan alat
def tambah_paket():
	print("Silahkan Tambahkan Paket ")
	Nama_paket = input(color.b+(f"Masukkan Nama paket pemesanan baru: "+color.b))
	Nama_alat = input(color.b+("Masukkan Nama Alat pesanan baru: "+color.b))
	nomor_paket = len(paket_alat) + 1 #untuk menambahkan panjang paket dan tambah 1
	paket_alat[nomor_paket] = {#untuk menambahkan data paket ke dalam paket alat dictionary dengan 3 key
	"Nama Paket": Nama_paket, 
	"Alat": [Nama_alat],
	"Pesanan":""
	}
	print(color.r+(f"Paket {Nama_paket} Telah Ditambahkan ke Database")+color.r)

# Fungsi untuk menambahkan isi Paket Alat
def tambah_isi_paket():
	lihat_data_alat()
	nomor_paket = int(input(color.b+f"Masukkan nomor paket yang ingin di tambah : "+color.b))
	if nomor_paket in paket_alat: #kondisi untuk memeriksa apakah nomor_paket sudah ada di dictionary paket_alat
		nama_alat_baru = input(color.b+(f"Masukkan Nama Alat Baru: "))
		paket_alat[nomor_paket]['Alat'].append(nama_alat_baru) #menambahkan isi paket di dictionary paket alat dengan key nomor paket dan mengakses 'alat' di dalam paket alat
		print(color.b+("Data paket alat telah diperbarui."))
	else:
	 print(color.r+("Paket tidak ditemukan."))

# Fungsi user untuk Memesan paketannya
def pilih_pesanan():
	while True:
		lihat_data_alat() #untuk memanggil fungsi lihat data
		try:
			pilihan_paket = int(input("Pilih paket yang ingin dipesan (masukkan angka): "))
			if 1 <= pilihan_paket <= len(paket_alat): #kondisi nilai pilihan_paket kurang dari atau sama dengan jumlah paket-alat yang tersedia
				nomor_pesanan = len(paket_alat[pilihan_paket]['Pesanan']) + 1 #menghitung jumlah pesanan yang sudah ada dalam paket tersebut dan menambahkan 1 ke jumlah pesanan, sehingga kita mendapatkan nomor pesanan baru.
				nama_pemesan = input("Masukkan nama Anda: ")
				paket_alat[pilihan_paket]['Pesanan'].append({#untuk menambahkan pilihan paket ke dalam dictionary paket_alat dan mengakses 'Pesanan" di dalam dictionary paket alat
                    'Nomor Pesanan': nomor_pesanan,
                    'Nama Pemesan': nama_pemesan,
					'Pesanan' : nama_pemesan
                })
				print(f"Pesanan Anda untuk Paket {pilihan_paket} telah diterima dengan nomor pesanan {nomor_pesanan}.")
				break
			else:
				print("Pilihan paket tidak valid. Silakan coba lagi.")
		except ValueError:
			print("Masukkan angka yang valid.")

# Fungsi Update Paket Baru
def update_paket():
	lihat_data_alat()# Memanggil fungsi lihat_data_alat untuk menampilkan paket-paket yang tersedia
	nomor_paket = int(input("Masukkan nomor paket yang ingin di ubah: "))
	if nomor_paket in paket_alat: # Memeriksa apakah nomor_paket ada dalam dictionary paket_alat
		paket_baru = input("Masukkan Paket Baru: ")
		paket_alat[nomor_paket]['Nama Paket'] = paket_baru #Untuk update paket dengan key nomor paket di dalam nama paket dengan paket baru
	else:
		print("Paket Tidak ditemukan")

# Fungsi Mengupdate Alat baru
def update_isi_paket():
	lihat_data_alat()# Memanggil fungsi lihat_data_alat untuk menampilkan paket-paket yang tersedia
	nomor_paket = int(input("Masukkan nomor paket yang ingin diupdate: "))
	if nomor_paket in paket_alat:# Memeriksa apakah nomor_paket ada dalam dictionary paket_alat
		print(f"Alat pada Paket {nomor_paket}:")
		for index, alat in enumerate(paket_alat[nomor_paket]['Alat'], start=1):#Melakukan perulangan melalui daftar alat dalam paket, dimulai dari nomor urutan 1.
			print(f"{index}. {alat}")
		pilihan_alat = int(input("Pilih nomor alat yang ingin diupdate (masukkan angka): "))
		if 0 < pilihan_alat <= len(paket_alat[nomor_paket]['Alat']):#kondisi pilihan alat kurang dari 0 dan kurang dari sama dengan jumlah alat dalam paket
			nama_alat_baru = input("Masukkan Nama Alat Baru: ")
			paket_alat[nomor_paket]['Alat'][pilihan_alat - 1] = nama_alat_baru#untuk mengganti nilai (nama alat) pada posisi tertentu dalam list 'Alat' yang terkait dengan paket tertentu.
			print("Data paket alat telah diperbarui.")
		else:("Pilihan Anda Tidak Valid")
	else:
		print("Paket tidak ditemukan.")

# fungsi Hapus Data Alat
def delete_alat():
	try:
		lihat_data_alat() #untuk melihat data alat atau memanggil fungsi lihat data alat
		nomor_paket = int(input("Masukkan nomor paket yang ingin dihapus alatnya: "))
		if nomor_paket in paket_alat: #memeriksa apakah nomor paket ada di dalam dictionary paket alat
			print(f"Alat pada Paket {nomor_paket}:")
			for index, alat in enumerate(paket_alat[nomor_paket]['Alat'], start=1):#perulangan untuk daftar alat dalam paket, di mulai dari nomor urutan 1
				print(f"{index}. {alat}")
			try:
				pilihan_alat = int(input("Pilih nomor alat yang ingin dihapus (masukkan angka) : "))
				if 0 < pilihan_alat <= len(paket_alat[nomor_paket]['Alat']):#kondisi pilihan alat kurang dari 0 dan kurang dari sama dengan jumlah alat dalam paket alat, dengan nomor alat sebagai key dan alat sebagai value
					alat_terhapus = paket_alat[nomor_paket]['Alat'].pop(pilihan_alat - 1)
					print(f"Alat '{alat_terhapus}' telah dihapus dari Paket {nomor_paket}.")
				elif pilihan_alat == 0:#Jika pilihan_alat (input yang dimasukkan oleh pengguna) sama dengan 0, maka kondisi ini akan dievaluasi sebagai benar.
					return
				else:
					print("Pilihan alat tidak valid.")
			except ValueError:
				print("Masukkan angka yang valid.")
		else:
			print("Paket tidak ditemukan.")
	except ValueError:print("Mohon Masukkan Angka")

# Hapus Paket
def delete_pesanan():
	try:
		lihat_data_alat()
		nomor_paket = int(input("Masukkan nomor paket yang ingin dihapus: "))
		if nomor_paket in paket_alat: #memeriksa apakah nomor paket sudah ada di dalam dictionary paket alat
			del paket_alat[nomor_paket] #menghapus nomor paket yang ada di dictionary paket alat
			print(f"Paket nomor {nomor_paket} telah dihapus.")
		else:
			print("Paket tidak ditemukan.")
	except ValueError:print("Mohon Masukkan Angka")

# Hapus Pesanan User
def delete_pesanan_user():
	lihat_data_pemesanan_user()
	try:
		nomor_paket = int(input("Masukkan nomor paket untuk menghapus pesanan: "))
		if nomor_paket in paket_alat: #memeriksa apakah nomor paket sudah ada di dalam dictionary paket alat
			pesanan = paket_alat[nomor_paket]['Pesanan'] #digunakan untuk mengakses list 'Pesanan' yang terkait dengan paket tertentu dalam dictionary paket_alat, dan nilai tersebut disimpan dalam variabel pesanan.
			if pesanan: #kondisi pesanan
				nomor_pesanan = int(input("Masukkan nomor pesanan yang ingin dihapus: "))#nomor pesanan yang akan di hapus
				for item in pesanan: #setiap perulangan, nilai dari list pesanan akan diambil dan disimpan dalam variabel item.
					if item['Nomor Pesanan'] == nomor_pesanan: #suatu kondisi Jika nilai dari key 'Nomor Pesanan' pada elemen yang sedang melakukan perulangan saat ini dalam list pesanan sama dengan nilai dari variabel nomor_pesanan, maka blok kode di dalam kondisi ini akan dieksekusi.
						pesanan.remove(item) #mengahapus pesanan dengan parameter item
						print("tekan enter untuk lanjut")
						input()
						print(f"Pesanan dengan nomor pesanan {nomor_pesanan} dihapus dari paket {nomor_paket}.")
						break
				else:
					print(f"Pesanan dengan nomor pesanan {nomor_pesanan} tidak ditemukan dalam paket {nomor_paket}.")
			else:
				print("Belum ada pesanan untuk paket ini.")
		else:
			print("Paket tidak ditemukan.")
	except ValueError:print("Mohon Masukkan Angka")
		
		

# fungsi menu Utama
def main_menu():
	os.system("cls")
	while True:
		try:
			grafiti()
			print("======================= Menu Utama ===================")
			print("|                  [1]  Registrasi                   |")
			print("|                  [2]  Login sebagai Admin          |")
			print("|                  [3]  Login sebagai User           |")
			print("|                  [4]  Keluar                       |")
			print("======================================================")
			pilih_menu = str(input(f"Masukkan Menu Pilihan Anda [1/2/3/4] : "))
			if pilih_menu == "1":
				print("SILAHKAN REGISTRASI............................")
				time.sleep(2)
				os.system("cls")
				registrasi()
			elif pilih_menu == "2":

				print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA...........................")
				time.sleep(2)
				os.system("cls")
				login_admin()
			elif pilih_menu == "3":
				print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA...........................")
				time.sleep(2)
				os.system("cls")
				login_user()
			elif pilih_menu == "4":
				time.sleep(3)
				exit()
			else: os.system("cls")
			print(color.r+"Pilihan Anda Tidak Valid"+color.r)#eror handling ketika pilihan di luar dari 3
		except ValueError: 
			os.system("cls")
			print(color.r+"Mohon masukkan Angka"+color.r)#eror hendling ketika di luar dari pilihan
# fungsi Menu Admin
def menu_admin():
	while True :
		try:
			print(color.b+"============================ SELAMAT DATANG DI MENU ADMIN ============================"+color.b)
			os.system("cls")
			print(color.b+f"============================ MENU ADMIN ============================"+color.b)
			print("|         [1] Lihat Data pemesanan 		                   |")
			print("|         [2] Lihat Deskripsi Paket Alat Sound System              |")
			print("|         [3] Menambahkan Paket Pemesanan Alat Sound System        |")
			print("|         [4] Memperbarui Data Paket Pemesanan Alat Sound System   |")
			print("|         [5] Hapus Data Pemesanan User                            |")
			print("|         [6] Hapus Deskripsi Paket Alat Sound System        	   |")
			print("|         [7] KembalI ke Menu Awal                                 |")
			print(color.b+"===================================================================="+color.b)
			pilih_menu = str(input("Silahkan Pilih Menu {1/2/3/4/5/6/7} : "))
			try:
				if pilih_menu == "1" : #untuk melihat data pemesanan
					logo_sound()
					time.sleep(1)
					lihat_data_pemesanan_user()
					print("\nTekan [ENTER] untuk Kembali.........")
					input()
					time.sleep(2)
				elif pilih_menu == "2" : #untuk melihat deskripsi paket alat sound system
					logo_sound()
					time.sleep(1)
					lihat_data_alat()
					print("\nTekan [ENTER] untuk Kembali.........")
					input()
					time.sleep(2)
				elif pilih_menu == "3": #untuk menambahkan paket pemesanan alat sound system
					while True:
						try:
							print("1. Menambahkan Paket Alat\n2. Menambahkan isi Paket Alat\n3. Kembali ke menu admin")
							pilihan_3 = int(input("Masukkan pilihan Anda {1/2/3} : "))
							if pilihan_3 == 1: #untuk menambahkan Paketan alat
								lihat_data_alat()
								time.sleep(1)
								tambah_paket()
							elif pilihan_3 == 2: #untuk menambahkan Isi Paketan alat
								lihat_data_alat()
								time.sleep(1)
								tambah_isi_paket()
							elif pilihan_3 == 3: #keluar dan akan mengembalikan ke menu admin
								logo_sound()
								os.system("cls")
								print("Mengembalikan ke Menu admin.........")
								time.sleep(4)
								menu_admin()
							else: os.system("cls")
							print(color.r+"Pilihan Anda Tidak Valid"+color.r)#eror handling ketika pilihan di luar dari 3
						except ValueError: 
							os.system("cls")
							print(color.r+"Mohon masukkan Angka"+color.r)#eror handling ketika pilihan di luar dari 3
				elif pilih_menu == "4":#untuk memperbarui data paket pemesanan alat sound system
					while True:
						os.system("cls")
						time.sleep(1)
						try:
							logo_sound()
							print(color.b+"1. Update Paket\n2. Update isi Paket\n3. Kembali ke menu admin"+color.b)
							pilih_Paket = int(input(color.g+"Masukkan Pilihan anda {1/2/3}: "+color.y))
							try:
								if pilih_Paket == 1: #Untuk mengupdate Paketan
									time.sleep(1)
									update_paket()
								elif pilih_Paket == 2:#untuk mengupdate isi paket
									print(color.b+"\nTekan [ENTER] Untuk Lanjut........."+color.b)
									input()		
									time.sleep(1)	
									lihat_data_alat
									time.sleep(1)
									update_isi_paket()
								elif pilih_Paket == 3:#keluar dari pilihan dan kembali ke menu admin
									logo_sound()
									os.system("cls")
									print("Mengembalikan ke Menu admin.........")
									time.sleep(4)
									menu_admin()
								else: print(color.r+"Pilihan Anda Tidak Valid"+color.r)
							except ValueError: print(color.r+"Mohon masukkan Angka"+color.r)
						except ValueError: 
							print(color.r+"Mohon masukkan Angka"+color.r)#eror hendling ketika di luar dari pilihan
				elif pilih_menu == "5":
					logo_sound()
					print(color.b+("\nTekan [ENTER] Untuk Lanjut........."+color.b))
					input()		
					time.sleep(2)	
					delete_pesanan_user()
				elif pilih_menu == "6" :
					while True :
						try:
							logo_sound()
							print("1. Delete Paket\n2. Delete Alat\n3. Kembali Ke Menu Admin")
							pilihan = int(input("Masukkan pilihan Anda {1/2/3}: "))
							time.sleep(1)
							if pilihan == 1:
								logo_sound()
								print(color.b+("\nTekan [ENTER] Untuk Lanjut........."+color.b))
								input()
								os.system("cls")
								time.sleep(1)
								lihat_data_alat
								time.sleep(1)
								delete_pesanan()
							elif pilihan == 2:
								logo_sound()
								print(color.b+("\nTekan [ENTER] Untuk Lanjut........."+color.b))
								input()
								time.sleep(1)
								lihat_data_alat()
								time.sleep(1)
								delete_alat()
							elif pilihan == 3:
								os.system("cls")
								print("Mengembalikan ke Menu admin.........")
								time.sleep(4)
								menu_admin()
							else:os.system("cls") 
							print("pilihan Anda Tidak Valid")
						except ValueError: 
							os.system("cls")
							print(color.r+("Mohon masukkan Angka")+color.r)
				elif pilih_menu == "7" :
					os.system("cls")
					print("Mengembalikan ke Menu Utama.........")
					time.sleep(2)
					main_menu()
				else: print(color.r+"Pilihan Anda Tidak Valid"+color.r)
			except ValueError:print(color.r+"Mohon Masukkan Angka"+color.r)
		except ValueError: 
			print(color.r+"Mohon masukkan Angka"+color.r)

# fungsi Menu User
def menu_user():
	while True:
		grafiti()
		try:
			print(color.b+f"============================ Menu User ============================")
			print("|        1. Tampilkan Paket Pemesanan Alat Sound System           |")
			print("|        2. Melakukan Pemesanan Paket                             |")
			print("|        3. Kembali ke Menu Awal                                  |")
			print("="*67)
			pilihan_menu = str(input("Masukkan Pilihan Anda {1/2/3}: "))
			time.sleep(1)
			if pilihan_menu == "1":
				logo_sound()
				time.sleep(1)
				lihat_data_alat()
				print("\nTekan [ENTER] untuk Kembali.........")
				input()
				os.system("cls")
				time.sleep(2)
			elif pilihan_menu == "2":
				os.system("cls")
				logo_sound()
				print("\nTekan [ENTER] Untuk Lanjut.........")
				input()
				time.sleep(1)
				pilih_pesanan()
				os.system("cls")
				time.sleep(1)
			elif pilihan_menu == "3":
				grafiti()
				print("Mengembalikan ke Menu Utama.........")
				os.system("cls")
				time.sleep(3)
				main_menu()
			else: print(color.r+"Pilihan Anda Tidak Valid"+color.r)
		except ValueError: 
			os.system("cls")
			print(color.r+"Mohon masukkan Angka"+color.r)

main_menu() #untuk memanggil fungsi utama



