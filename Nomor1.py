tinggi_piramida = int(input("Input Tinggi Piramida: "))

for i in range(tinggi_piramida):
  # Mencetak spasi
  for j in range(tinggi_piramida - i - 1):
    print(' ', end = '')

  # Mencetak bintang
  for k in range(i + 1):
    print('* ', end = '')
  
  # Ganti baris selanjutnya
  print()