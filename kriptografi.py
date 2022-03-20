

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

#fungsi enkripsi dengan parameter abjad
def enkripsi(abjad): 
    kalimat = input("Kalimat : ") 
    key = int(input("Key : ")) 

    kalimat = kalimat.lower() 
    hasil = '' 

    for char in kalimat: 
      if char in abjad: 
        n = abjad.index(char) 
        encrypt = (n - key) % 26 
        convert = abjad[encrypt]
        hasil = hasil + convert 
      else:
          hasil = hasil + ' ' 

    print(f"Hasil : {hasil}") 

#fungsi dekripsi dengan parameter abjad
def dekripsi(abjad):
    kalimat = input("Kalimat Enkripsi : ")  
    key = int(input("Key : ")) 

    kalimat = kalimat.upper() 
    hasil = '' 
    for char in kalimat: 
        if char in abjad: 
          n = abjad.index(char) 
          encrypt = (n + key) % 26 
          convert = abjad[encrypt] 
          hasil = hasil + convert
        else:
            hasil = hasil + ' '  

    print(f"Hasil : {hasil}") 

#menampilkan menu
pilihan = 'y' 

while (pilihan == 'y'): 
  print("Menu : ")
  print("1. Enkripsi Data")
  print("2. Dekripsi Data")
  print("3. Keluar")

  menu = input("Pilihan Menu : ")

  if menu == '1': 
    enkripsi(abjad) 
  elif menu == '2': 
    dekripsi(abjad) 
  elif menu == '3':
    print("progam selesai, terima kasih")
    break 
  else:
    print("Menu tidak ditemukan") 
