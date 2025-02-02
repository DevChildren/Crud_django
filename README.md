```markdown
Template blog ini dibangun menggunakan Django dan Bootstrap, menyediakan berbagai fitur penting untuk membangun blog yang fungsional dan modern. Fitur-fitur utama termasuk like, komentar, berbagi artikel, dan pengelolaan konten melalui Dashboard Admin Django.

## Fitur Utama

- **Dashboard Admin Bawaan Django**  
  Pengelolaan blog dan artikel menggunakan dashboard admin Django yang kuat dan mudah digunakan.

- **Desain Responsif dengan Bootstrap**  
  Tampilan blog menggunakan Bootstrap untuk memastikan responsivitas di perangkat desktop maupun mobile.

- **Like Post**  
  Pengguna yang login dapat memberi "like" pada artikel yang mereka sukai.

- **Komentar Post**  
  Pengguna yang login dapat berkomentar pada artikel.

- **Share Post**  
  Pengguna dapat membagikan artikel ke platform lain.

- **Subscribe dan Unsubscribe**  
  Pengguna dapat berlangganan untuk menerima pembaruan artikel terbaru dan berhenti berlangganan kapan saja.

- **Notifikasi Email**  
  Subscriber akan menerima email ketika admin memposting artikel baru.

- **Login, Registrasi, dan Forgot Password**  
  Fitur login, pendaftaran akun, dan pengaturan ulang password.

- **Pencarian Artikel**  
  Pengguna dapat mencari artikel berdasarkan kata kunci.

- **Post Berdasarkan Kategori**  
  Artikel dikelompokkan berdasarkan kategori untuk memudahkan pencarian.

- **Light dan Dark Mode**  
  Pengguna dapat memilih tampilan antara mode terang (light mode) atau gelap (dark mode).

## Instalasi

1. **Kloning Repository ini**  
   Gunakan perintah berikut untuk mengkloning repository ini ke komputer Anda:

   ```bash
   git clone https://github.com/username/repository-name.git
   ```

2. **Instalasi Dependensi**  
   Pastikan Anda telah menginstal Python dan pip. Kemudian, jalankan perintah berikut untuk menginstal dependensi yang diperlukan:

   ```bash
   cd blog-django
   pip install -r requirements.txt
   ```

3. **Konfigurasi Pengaturan Database**  
   Sesuaikan pengaturan database di `settings.py` jika diperlukan. Pastikan Anda sudah mengonfigurasi database seperti SQLite, PostgreSQL, atau MySQL.

4. **Migrasi Database**  
   Jalankan perintah berikut untuk membuat tabel dan struktur database yang diperlukan:

   ```bash
   python manage.py migrate
   ```

5. **Menjalankan Server**  
   Setelah selesai dengan migrasi, jalankan server Django lokal:

   ```bash
   python manage.py runserver
   ```

6. **Akses Blog di Browser**  
   Buka browser dan akses blog Anda di `http://127.0.0.1:8000/`.


## Cara Penggunaan

Setelah template blog ini diinstal, Anda dapat menyesuaikan dan mengonfigurasi berbagai fitur sesuai kebutuhan:

- **Mengelola Artikel**: Masuk ke dashboard admin untuk membuat, mengedit, dan menghapus artikel.
- **Mengelola Pengguna**: Atur pengguna dan izin mereka melalui admin panel Django.
- **Menyesuaikan Tampilan**: Modifikasi tampilan menggunakan file CSS dan template HTML sesuai preferensi desain Anda.

## Lisensi

Template blog ini dilisensikan di bawah [MIT License](LICENSE).

---

Terima kasih telah memilih blog Django ini! Semoga bermanfaat untuk proyek Anda. Jika Anda memiliki pertanyaan atau masalah, silakan buka [issue di GitHub](https://github.com/username/repository-name/issues).
```
