# Atur cara menentukan penempatan kelas

nama = str(input("Masukkan nama anda:"))
markah = float(input("Masukkan markah anda:"))

# Kategori kelas
if markah <= 40:
     print("Anda ditempatkan di Kelas Dedikasi.")
elif markah <= 60:
     print("Anda ditempatkan di Kelas Cerdik.")
elif markah <= 80:
     print("Anda ditempatkan di Kelas Bijak.")
else:
     print("Anda ditempatkan di Kelas Amanah.")
