# class
class mahasiswa():
    def __init__(self, input_nim, input_nama, input_nilai):
        self.nim = input_nim
        self.nama = input_nama
        self.nilai = input_nilai

print("============== Data Mahasiswa ==============")
print("============================================Tambah dan Tampilkan============================================")
print("Mahasiswa 1")
jay = mahasiswa("Nim: 01234567", "Nama: jaynaludin", "Nilai: 90")
print(jay.nim)
print(jay.nama)
print(jay.nilai)

print("============================================")

print("Mahasiswa 2")
keeho = mahasiswa("Nim: 08975634", "Nama: yoon keeho", "Nilai: 100")
print(keeho.nim)
print(keeho.nama)
print(keeho.nilai)

print("============================================")

print("Mahasiswa 3")
kai = mahasiswa("Nim: 04689216", "Nama: kai ahmad", "Nilai: 95")
print(kai.nim)
print(kai.nama)
print(kai.nilai)

print("============================================")

print("Mahasiswa 4")
jeno = mahasiswa("Nim: 07981034", "Nama: lee jeno", "Nilai: 80")
print(jeno.nim)
print(jeno.nama)
print(jeno.nilai)


print("============================================Hapus Data============================================")

list_nama = ["Nama: jaynaludin, Nilai: 90", "Nama: yoon keeho, Nilai: 100", "Nama: kai ahmad, Nilai: 95", "Nama: lee jeno, Nilai: 80"]
print (list_nama)

nama_yang_terhapus = list_nama.pop(1)

print('nama yang terhapus:', nama_yang_terhapus)
print (list_nama)


print("============================================Mengubah Data============================================")

list_nama = ["Nama: jaynaludin, Nilai: 90", "Nama: yoon keeho, Nilai: 100", "Nama: kai ahmad, Nilai: 95", "Nama: lee jeno, Nilai: 80"]
print (list_nama)

nama_yang_ditambahkan = list_nama.append('Nama: jung jaehyun, Nilai: 99')

print('nama yang ditambahkan:')
print(list_nama)
