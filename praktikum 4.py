def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir berdasarkan bobot komponen nilai"""
    return tugas * 0.30 + uts * 0.35 + uas * 0.35

def main():
    data_mahasiswa = []  # List untuk menyimpan data mahasiswa
    
    while True:
        # Meminta input data mahasiswa
        nama = input("Masukkan nama mahasiswa: ")
        nim = input ("Nim: ")
        
        # Menangani kesalahan input untuk nilai
        try:
            tugas = float(input("Masukkan nilai tugas: "))
            uts = float(input("Masukkan nilai UTS: "))
            uas = float(input("Masukkan nilai UAS: "))
        except ValueError:
            print("Nilai harus berupa angka! Silakan masukkan kembali.")
            continue
        
        # Menghitung nilai akhir
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        
        # Menyimpan data mahasiswa dalam bentuk dictionary
        data_mahasiswa.append({
            'nama': nama,
            'nim': nim,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        })
        
        # Menanyakan apakah ingin menambah data lagi
        tambah_data = input("Apakah Anda ingin menambah data (y/t)? ").lower()
        
        # Jika jawabannya 't', keluar dari loop
        if tambah_data == 't':
            break
    
    # Menampilkan daftar data mahasiswa
    print("\nDaftar Data Mahasiswa:")
    for data in data_mahasiswa:
        print(f"Nama: {data['nama']}")
        print(f"Nilai Tugas: {data['tugas']}")
        print(f"Nilai UTS: {data['uts']}")
        print(f"Nilai UAS: {data['uas']}")
        print(f"Nilai Akhir: {data['nilai_akhir']:.2f}")
        print("-" * 30)

# Menjalankan program
if __name__ == "__main__":
    main()
