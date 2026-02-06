# 📦 TechMaster – Sistem Manajemen Inventaris Elektronik (OOP Python)

Proyek ini merupakan tugas pemrograman Python yang menerapkan **4 Pilar OOP**  
(Abstraction, Encapsulation, Inheritance, dan Polymorphism) untuk membuat sistem
manajemen inventaris sederhana pada toko elektronik bernama **TechMaster**.

## 🎯 Tujuan Proyek
Membangun backend sederhana untuk:
- Mengelola stok barang elektronik
- Menghitung harga + pajak secara otomatis
- Menampilkan detail transaksi

## 🧱 Konsep OOP yang Digunakan

1. **Abstraction**  
   Menggunakan Abstract Class `BarangElektronik` dengan method:
   - `tampilkan_detail()`
   - `hitung_harga_total(jumlah)`

2. **Encapsulation**  
   Atribut sensitif seperti `__stok` dan `__harga_dasar` dibuat private dan
   hanya bisa diakses melalui method.

3. **Inheritance**  
   Class `Laptop` dan `Smartphone` mewarisi `BarangElektronik`.

4. **Polymorphism**  
   Method yang sama (`tampilkan_detail`, `hitung_harga_total`) memiliki perilaku
   berbeda pada setiap class anak.

## 🛒 Skenario Program
1. Admin membuat data produk Laptop dan Smartphone.  
2. Admin menambah stok (stok negatif ditolak).  
3. User membeli 2 Laptop dan 1 Smartphone.  
4. Program menampilkan struk transaksi dan total tagihan.

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall.
2. Jalankan perintah berikut di terminal:

```bash
python techmaster.py
