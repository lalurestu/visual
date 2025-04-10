---
# Font Size and Color Adjuster
## Oleh: Lalu Restu Bagus Anugrah (F1D022059)

Aplikasi berbasis GUI ini dikembangkan menggunakan **PyQt5** dengan fungsi utama untuk mengatur ukuran teks, warna font, dan warna latar belakang melalui kontrol slider. Teks utama yang dapat dimodifikasi adalah NIM mahasiswa, sedangkan nama mahasiswa ditampilkan sebagai informasi di bagian atas antarmuka. Semua perubahan yang dilakukan akan langsung terlihat secara real-time.
---

## Penjelasan Per Fungsi

### `__init__(self)`

Fungsi `__init__` adalah konstruktor utama yang bertanggung jawab untuk mengatur seluruh tampilan aplikasi. Tahap inisialisasi dimulai dengan penetapan judul dari jendela dan dimensi awal yang berukuran 500×400 piksel. Setelah itu, dibuat widget utama yang menggunakan layout vertikal sebagai tempat untuk semua komponen tampilan. Label yang menunjukkan identitas pengembang ditambahkan di bagian atas sebagai informasi pengantar. Elemen penting `display_label` diatur sebagai area teks utama dengan pengaturan awal mencakup ukuran font sebesar 30 poin, warna teks hitam, dan latar belakang putih. Setelah itu, ketiga fungsi yang membuat slider dipanggil untuk menyelesaikan desain antarmuka. Di akhir, nilai default seluruh slider diatur agar aplikasi dapat langsung digunakan saat pertama kali dijalankan.

### `create_font_size_slider(self, layout)`

Fungsi ini adalah fungsi yang membuat dan menyesuaikan slider yang mengatur ukuran huruf. Dengan memanfaatkan `QHBoxLayout`, semua elemen kontrol disusun secara horizontal dalam satu baris teratur. Slider memiliki rentang nilai antara 20 hingga 60 poin, yang mewakili ukuran teks dari menengah hingga besar. Label yang menjelaskan "Ukuran Font" diletakkan di sisi kiri sebagai petunjuk fungsi, sementara label yang menunjukkan nilai saat ini ditempatkan di sebelah kanan untuk memberikan umpan balik visual. Proses pembaruan terhubung melalui sinyal `valueChanged` yang akan mengaktifkan fungsi `update_font_size` setiap kali nilai slider berubah, menjamin bahwa perubahan ukuran teks terjadi secara langsung.

### `create_font_color_slider(self, layout)`

Fungsi ini memperkenalkan kontrol slider untuk mengubah warna teks melalui skala grayscale. Seperti halnya komponen slider lainnya, antarmuka disusun secara horizontal dengan label penjelas, slider kontrol, dan tampilan nilai numerik. Rentang nilai yang digunakan adalah 0-255 untuk mencakup seluruh spektrum grayscale, di mana 0 menghasilkan teks hitam pekat, sementara 255 memberikan teks putih bersih. Desain sistem ini dibuat sederhana, tetapi tetap menawarkan cukup fleksibilitas untuk kebutuhan dasar pengaturan kontras teks. Setiap kali slider digeser, fungsi `update_colors` akan secara otomatis dipanggil untuk menangani perubahan warna.

### `create_bg_color_slider(self, layout)`

Slider warna latar belakang dibuat dengan metode yang serupa, namun dengan tujuan yang berbeda. Dengan menggunakan layout horizontal yang seragam, komponen ini memberi kemampuan kepada pengguna untuk menyesuaikan warna latar dari hitam (0) hingga putih (255). Adanya indikator berupa angka memudahkan pengguna dalam melakukan penyesuaian yang tepat. Keterkaitan antara slider ini dan fungsi `update_colors` menjamin bahwa setiap perubahan nilai akan segera berdampak pada tampilan label utama. Penggabungan slider untuk warna teks dan latar belakang memungkinkan eksplorasi berbagai kombinasi kontras demi mencapai keterbacaan yang maksimal.

### `update_font_size(self, value)`

Fungsi ini diaktifkan setiap kali pengguna menggerakkan slider untuk mengubah ukuran font. Proses ini dimulai dengan mendapatkan objek font yang digunakan saat ini pada `display_label`, kemudian melakukan perubahan pada properti ukuran titik sesuai dengan nilai terbaru dari slider. Font yang telah disesuaikan kemudian diterapkan lagi pada label. Secara bersamaan, fungsi ini juga menyegarkan teks indikator yang menunjukkan ukuran saat ini. Mekanisme ini menjamin bahwa ukuran teks di label utama selalu sesuai dengan posisi slider dan nilai yang ditampilkan, memberikan umpan balik visual yang segera dan tepat bagi pengguna.

### `update_colors(self)`

Sebagai fungsi yang mengelola perubahan warna, `update_colors` beroperasi dengan mengambil nilai terbaru dari kedua slider (warna teks dan latar belakang). Nilai-nilai tersebut kemudian diolah menjadi string stylesheet CSS yang sah, memanfaatkan format grayscale RGB di mana ketiga elemen warna (merah, hijau, biru) mendapatkan nilai yang identik. Stylesheet ini segera diterapkan pada `display_label`, yang menghasilkan perubahan visual yang langsung terlihat. Fungsi ini juga bertugas untuk memperbarui teks pada indikator di kedua slider agar selalu mencerminkan nilai yang benar. Pendekatan terpadu ini menjaga konsistensi tampilan dan memudahkan pemeliharaan kode.

---

## 👀 Fitur Utama

- **Penyesuaian Ukuran Font Dinamis**: Rentang 20-60 point
- **Kontrol Warna Teks**: Skala grayscale penuh
- **Kustomisasi Latar Belakang**: Fleksibilitas penyesuaian kontras
- **Respons Real-time**: Perubahan langsung terlihat tanpa perlu proses tambahan

---
