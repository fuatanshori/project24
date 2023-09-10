# Company Profile Website

Ini adalah proyek Company Profile Website yang dikembangkan menggunakan Django. Proyek ini bertujuan untuk memungkinkan perusahaan untuk mempresentasikan informasi mereka kepada calon pelanggan dan mitra bisnis.

## Cara Menjalankan Aplikasi

Berikut adalah langkah-langkah untuk menjalankan aplikasi ini di lingkungan pengembangan Anda:

1. Instal semua dependensi yang dibutuhkan dengan menjalankan perintah berikut:
    pip install -r requirements.txt
2. Migrasikan basis data dengan menjalankan perintah berikut:
   python manage.py migrate
3. Buat superuser untuk mengelola konten situs web dengan perintah:
   python manage.py createsuperuser
4. Kumpulkan file statis dengan perintah berikut:
   python manage.py collectstatic
5. Terakhir, jalankan server pengembangan dengan perintah:
   python manage.py runserver


Sekarang, Anda dapat mengakses aplikasi Company Profile Website melalui browser web Anda dengan mengunjungi [http://localhost:8000/](http://localhost:8000/).
Pastikan Anda memiliki Python dan pip terinstal di sistem Anda sebelum menjalankan perintah-perintah di atas. Selain itu, pastikan Anda telah mengkonfigurasi pengaturan database yang sesuai di file `settings.py` jika diperlukan.

