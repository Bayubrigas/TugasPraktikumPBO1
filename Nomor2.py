jumlah_siswa = int(input("Masukkan jumlah siswa: "))

dictionary = {}

for i in range(1, jumlah_siswa + 1):
    nama_siswa = input(f"Masukkan nama siswa ke-{i}: ")
    nilai_siswa = int(input(f"Masukkan nilai untuk {nama_siswa}: "))
    dictionary[nama_siswa] = nilai_siswa
    
print("Hasil =", dictionary)
