#INPUT LIST NAMA DAN JABATAN
Nama =["Ketua: Muhammad Faris", "Wakil: Ananda Ion Jahfal", "Sekretaris: Nadya Kusuma Astuti", "Bendahara: Zessiva Isma Putri"]


#MENU UTAMA PROGRAM
print ("---------------------------------------------------------")
print ("Halo Pengguna!")
print ("Selamat Datang di Sistem Informasi Keanggotaan BEMFT 2025")
print ("---------------------------------------------------------")
print ("Menu Utama: ")
print ("1. Tambah Anggota BEM FT 2025")
print ("2. Perbarui Anggota BEM FT 2025")
print ("3. Tampilkan Anggota BEM FT 2025")
print ("4. Hapus Anggota BEM FT 2025")
print ("---------------------------------------------------------")

#PEMILIHAN MENU
pilihan =input("Apa yang ingin anda lakukan? ")

#KONSEP CREATE
if pilihan == '1':
    anggota_baru = input("Masukkan Jabatan dan Nama (Jabatan: Nama): ")
    if anggota_baru in Nama:
        print ("Jabatan sudah diisi. Silakan pilih menu 2 untuk memperbarui.")
    else:
        Nama.append(anggota_baru)     
        # Jabatan.append(jabatan_baru)
        print (f"Selamat! Anda berhasil menambahkan {anggota_baru} pada keanggotaan BEM FT 2025")
        print ("-------------------------------------------------------------------------------")
        print ("Daftar Anggota BEM FT 2025:")
        print (Nama)

#KONSEP UPDATE
elif pilihan == '2':
    update =  input ("Masukkan Jabatan dan Nama yang ingin di update (Jabatan: Nama): ")
    if update in Nama:
        index= Nama.index(update)
        Nama [index] = input ("Masukkan Jabatan dan Nama yang baru (Jabatan: Nama): ")
        print (f"Posisi {update} kini digantikan oleh {Nama[index]}")
        print ("---------------------------------------------------")
        print ("Daftar Anggota BEM FT 2025")
        print (Nama)
    else:
        print ("Jabatan dan nama yang anda masukkan tidak valid")
    

#KONSEP READ

elif pilihan == '3':
    print ("-------------------------------------")
    print ("Daftar Anggota BEM FT 2025:")
    print (Nama)


#KONSEP DELETE
elif pilihan == '4':
    hapus = input("Masukkan Jabatan dan Nama yang ingin dihapus (Jabatan: Nama): ")
    if hapus in Nama:
        index = Nama.index(hapus)
        Nama.remove(Nama[index])
        print ("-------------------------------------------------------------")
        print (f"{hapus} tidak lagi terdaftar sebagai bagian dari BEMFT 2025 ")
        print("Silakan pilih menu 1 untuk menambahkan anggota baru.")
        print ("-------------------------------------")
        print ("Daftar Anggota BEM FT 2025")
        print (Nama)
    else:
        print("Nama tersebut tidak terdaftar pada Keanggotaan BEM FT 2025")
else:
    print ("Pilihan yang anda masukkan tidak valid")