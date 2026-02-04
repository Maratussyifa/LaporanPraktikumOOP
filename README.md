🔹 Analisis 1 – Atribut & Object

Pertanyaan:
Apa yang terjadi jika hero1.hp = 500 setelah objek dibuat?

Jawaban:
Nilai HP pada objek hero1 akan berubah menjadi 500.
Ini menunjukkan bahwa atribut public bisa diubah langsung dari luar class.

📌 Kesimpulan:
Tanpa enkapsulasi, data mudah dimodifikasi secara bebas dan berisiko merusak logika game.

🔹 Analisis 2 – Interaksi Antar Objek

Pertanyaan:
Mengapa parameter lawan pada method serang harus berupa objek, bukan string?

Jawaban:
Karena kita butuh memanggil method diserang() milik objek lawan.
Jika hanya string nama, maka tidak ada data HP atau method yang bisa diproses.

📌 Kesimpulan:
Objek menyimpan data + perilaku, bukan sekadar teks.
<img width="1920" height="1008" alt="Screenshot 2026-02-04 090918" src="https://github.com/user-attachments/assets/957d7aed-2a7f-4ead-81ce-0c3fb152e266" />


🔹 Analisis 3 – Fungsi super()

Pertanyaan:
Apa error jika super().__init__() dihapus di class Mage?

Jawaban:
Error yang muncul:

AttributeError: 'Mage' object has no attribute 'name'


Penjelasan:
Karena constructor milik Hero tidak dijalankan, atribut name, hp, dan attack_power tidak dibuat di Mage.

📌 Peran super():

Menghubungkan data dari class Induk ke Anak

Memastikan Mage tetap punya atribut Hero
<img width="1920" height="1008" alt="Screenshot 2026-02-04 091122" src="https://github.com/user-attachments/assets/203d8dbe-f5d2-4106-bf6c-1e7d9780c424" />


🔹 Analisis 4 – Enkapsulasi (Getter & Setter)
1️⃣ Percobaan Akses Paksa
hero1._Hero__hp

Hasil:
Nilai HP muncul.
Penjelasan:
Python menggunakan Name Mangling (__hp → _Hero__hp).
Namun secara standar OOP, atribut private tidak boleh diakses langsung.

2️⃣ Setter Tanpa Validasi

Jika setter hanya:
self.__hp = nilai_baru
Lalu dipanggil:
hero1.set_hp(-100)
Hasil:
HP menjadi -100.

📌 Kesimpulan:
Setter penting untuk menjaga integritas data agar:
Tidak negatif
Tidak curang

Tetap logis dalam game

🔹 Analisis 5 – Abstraction & Interface
1️⃣ Melanggar Kontrak

Jika method serang() di Hero dihapus:
Error:

TypeError: Can't instantiate abstract class Hero with abstract method serang
Artinya:
Hero belum memenuhi kontrak dari GameUnit, jadi tidak boleh jadi objek.

📌 Konsekuensi:

Class tidak bisa digunakan
Program error

2️⃣ GameUnit Jadi Objek
Jika:
unit = GameUnit()


Error:

TypeError: Can't instantiate abstract class GameUnit...
📌 Penjelasan:
GameUnit adalah blueprint, bukan objek nyata.

📌 Gunanya:

Menyeragamkan struktur class
Memaksa semua unit punya method wajib

🔹 Analisis 6 – Polymorphism
1️⃣ Tambah Class Healer
Healer ditambahkan ke pasukan tanpa mengubah loop.

Hasil:
Program tetap berjalan lancar.

📌 Kesimpulan:
Polimorfisme memudahkan pengembangan game:
Tambah karakter baru tanpa ubah sistem lama
Kode fleksibel & scalable

2️⃣ Ubah serang → tembak_panah di Archer

Hasil:
Program error:
AttributeError: 'Archer' object has no attribute 'serang'
📌 Penjelasan:
Dalam Polimorfisme, semua child class harus punya nama method yang sama dengan parent.

output analisis 3-6 !
<img width="1920" height="1008" alt="Screenshot 2026-02-04 091351" src="https://github.com/user-attachments/assets/f0487466-1912-4aec-9d6d-43b11012bfcf" />
