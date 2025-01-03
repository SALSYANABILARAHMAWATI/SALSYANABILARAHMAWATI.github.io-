from metaflow import FlowSpec, step

class KuliahInformatikaFlow(FlowSpec):
    
    @step
    def start(self):
        # Inisialisasi Tugas Final Project METOPEN
        self.nama_mahasiswa = "Salsya Nabila Rahmawati"
        self.judul_project = False
        print(f"Memulai alur untuk Final Project: {self.nama_mahasiswa}")
        self.next(self.judul_project)

    @step
    def bayar_spp(self):
        # Langkah untuk membuat judul project
        self.judul_project = True
        print(f"{self.nama_mahasiswa} sudah bisa diakses.")
        self.next(self.memulai_judul_project)

    @step
    def memulai_judul_project(self):
        # Langkah untuk memulai membuat judul project 
        if not self.memulai_judul_project:
            print(f"{self.nama_mahasiswa} harus membuat judul project terlebih dahulu.")
            self.next(self.end)
        else:
            print(f"{self.nama_mahasiswa} memulai judul project baru.")
            self.next(self.dapatkan_nilai)

    @step
    def dapatkan_nilai(self):
        # Langkah untuk memberikan nilai akhir
        self.nilai_akhir = "A"
        print(f"{self.nama_mahasiswa} mendapatkan nilai akhir: {self.nilai_akhir}")
        self.next(self.end)

    @step
    def end(self):
        # Akhir dari alur kerja
        print("Alur kerja selesai untuk mahasiswa:", self.nama_mahasiswa)

if __name__ == "__main__":
    KuliahInformatikaFlow()