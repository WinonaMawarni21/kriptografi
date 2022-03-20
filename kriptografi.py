#rumus enkripsi = (n - key) % 26
#rumus dekripsi = (n + key) % 26
#n = merupakan urutan dari abjad yang diinput 
#key = merupakan kunci dekripsi atau enkripsi
#26 =merupakan jumlah dari seluruh abjad

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
#abjad berfungsi untuk menampung nilai abjad yang ada

#fungsi enkripsi dengan parameter abjad
def enkripsi(abjad): # membuat fungsi yang bertujuan untuk menerapkan caesar cipher
    kalimat = input("Kalimat : ") #input kalimat yang akan di enkripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (enkripsi)

    kalimat = kalimat.lower() #kalimat di konversi ke huruf kecil semua
    hasil = '' #membuat variable string untuk memuat hasil enkripsi

    for char in kalimat: #membuat perulangan untuk mengenkripsi kalimat
      if char in abjad: #abjad kalimat dipecah 1 1 dan di cek apakah terdapat dalam value abjad
        n = abjad.index(char) #jika ada maka nilai index dariabjad yang ditemukan disimpan dalam variable n
        encrypt = (n - key) % 26 #rumus enkripsi
        convert = abjad[encrypt] #konversi nilai string ke hasil enkripsi
        hasil = hasil + convert #membuat variable baru yang memuat hasil enkripsi
      else:
          hasil = hasil + ' ' #jika karakter yang dimasukkan bukan berasal dari abjad A - Z maka akan menjadi spasi

    print(f"Hasil : {hasil}") #hasil dari perulangan untuk enkripsi kalimat di tampilkan 

#fungsi dekripsi dengan parameter abjad
def dekripsi(abjad):
    kalimat = input("Kalimat Enkripsi : ")  #input kalimat yang akan di dekripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (dekripsi)

    kalimat = kalimat.upper() #kalimat di konversi ke huruf besar semua
    hasil = '' #membuat variable string untuk memuat hasil enkripsi

    for char in kalimat: #membuat perulangan untuk mengenkripsi kalimat
        if char in abjad: #abjad kalimat dipecah 1 1 dan di cek apakah terdapat dalam value abjad
          n = abjad.index(char) #jika ada maka nilai index dariabjad yang ditemukan disimpan dalam variable n
          encrypt = (n + key) % 26 #rumus dekripsi
          convert = abjad[encrypt] #konversi nilai string ke hasil dekripsi
          hasil = hasil + convert #membuat variable baru yang memuat hasil enkripsi
        else:
            hasil = hasil + ' '  #jika karakter yang dimasukkan bukan berasal dari abjad A - Z maka akan menjadi spasi

    print(f"Hasil : {hasil}") #hasil dari perulangan untuk enkripsi kalimat di tampilkan 

#menampilkan menu
pilihan = 'y' 

while (pilihan == 'y'): # membuat pilihan untuk melakukan enkripsi atau dekripsi
  print("Menu : ")
  print("1. Enkripsi Data")
  print("2. Dekripsi Data")
  print("3. Keluar")

  menu = input("Pilihan Menu : ")

  if menu == '1': # memasukkan kalimat yang akan di enkripsi
    enkripsi(abjad) # memanggil fungsi Caesar_cipher untuk mengenkripsi kalimat
  elif menu == '2': # memasukkan kalimat yang akan di enkripsi
    dekripsi(abjad) # memanggil fungsi Caesar_cipher untuk mendekripsi kalimat
  elif menu == '3':
    print("progam selesai, terima kasih")
    break 
  else:
    print("Menu tidak ditemukan") #jika memilih menu yang tidak ada di pilihan maka akan ditampilkan "menu tidak ditemukan" 
