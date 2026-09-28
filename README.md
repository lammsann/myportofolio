Nama : Ghulam Muhammad Ihsan

NPM : 2506656766

Kelas : PBP B

## Tugas 1

1. Ya dipakai, saya pakai section, section ini kugunakan untuk membagi halaman di html bagian per bagian, membagi bagian about me dengan skills. Hal ini membantu untuk membuat dan medesign bagian per bagian dengan lebih mudah serta memperbaikinya. Section juga lebih mudah dibaca jika proyeknya dikerjakan secara berkelompong (readable)
2. Trial error, mencoba coba padding yang pas, size dan lainnya serta mencari cari syntax agar bisa membuat webnya responsif. Saya kurang bisa untuk design dan mengatur elemen elemen agar sesuai dan bagus.
3. Misal mau tambah section portofolio, jika ada proyek baru maka harus ditambah manual di halaman htmlnya sehingga tidak efisien. Kedepannya jika sudah terintegrasi dengan database saya hanya perlu mengaksesnya dari backend tanpa perlu mengubah frontendnya.

   Saya tidak menggunakan AI pada Tugas 1 ini, yang saya lakukan ialah mencari syntax melalui google dan trial error

[sko.dev/snippet/cara-membuat-garis-di-html-css](https://sko.dev/snippet/cara-membuat-garis-di-html-css/)

[www.w3schools.com/css/css_grid.asp](https://www.w3schools.com/css/css_grid.asp)

## Tugas 2

1. Saat user akses /education, Django akan menerima request tersebut dan mengecek apakah url tersebut ada di urls.py, Setelah itu akan di routing oleh main/urls.py. Disana /education ditaruh pada function view show_education agar bisa dilihat. Function itu berguna untuk mengambil data dari database melalui model education. Setelah dapat datanya, akan dimunculkan pada web (response) ke user.
2. Menyimpan data pada model memudahkan kita untuk menambah atau mengelola. Jika melakukan hardcode di html setiap mau menambah projek baru atau education baru. harus mengubah html nya lagi. Kalau pake model untuk menambah, menghapus data lebih mudah melalui dashboard admin django tanpa perlu mengubah kode html.
3. makemigrations gunanya setiap kita mengubah atau menambah model (biar django tau ada data baru) dan masuk ke folder migrations, kalau migrate buat meneruskan data/hal yang ada di migrations untuk masuk ke database. Contoh: misal bikin model project dan fiel fieldnya. Pas dibuat di model (belum makemigrations) databasenya belum ada (baru dibuat pas makemigrations dan di migrate).

   Saya tidak menggunakan AI pada Tugas 2 ini, yang saya lakukan ialah menggunakan kode dari tutorial dan memodifikasinya

## Tugas 3

1. ModelForm sangat menghemat waktu karena secara otomatis membuat elemen form HTML berdasarkan struktur Field (kolom) yang sudah ada di Model database kita. Selain itu, ModelForm secara otomatis menangani validasi data (misalnya memastikan format email benar) tanpa perlu kita tulis ulang secara manual dari nol.
   Mengapa {% csrf_token %}: Ini adalah mekanisme keamanan untuk pencegahan serangan Cross-Site Request Forgery. Token ini berfungsi sebagai "kata sandi acak sementara" untuk memastikan bahwa data form yang dikirim (POST) benar-benar berasal dari website kita sendiri, bukan dari website peretas pihak ketiga yang mencoba memanipulasi request.
2. JSON lebih disukai karena format penulisannya jauh lebih ringan, ringkas, dan mudah dibaca oleh manusia dibandingkan XML yang butuh banyak tag pembuka dan penutup (mirip HTML). Selain itu, JSON bisa langsung diproses (parse) oleh JavaScript tanpa memerlukan tools tambahan karena format JSON pada dasarnya merupakan struktur objek asli (objek native) dari JavaScript.
3. Alur HTTP JSON: Saat client (browser) meminta data, fungsi view (misal: get_experience_json) akan mengambil data (QuerySet) dari database melalui Model. Data QuerySet tersebut kemudian di-Serialisasi menjadi bentuk JSON, lalu dibungkus dan dikembalikan (return) ke client melalui HttpResponse dengan tipe konten application/json.
   Alasan Serialisasi: Data yang diambil dari database Django masih berupa "Objek Python" yang rumit dan tidak bisa dikirim begitu saja lewat internet. Serialisasi adalah proses menerjemahkan "Objek Python" tersebut menjadi format teks standar (seperti JSON) agar bisa dibaca, dipahami, dan ditampilkan oleh sistem bahasa pemrograman lain di sisi client (seperti JavaScript di browser).

   AI Disclosure: [share.gemini.google/hBaUHc1Ih0vV](https://share.gemini.google/hBaUHc1Ih0vV)

## Tugas 4

AI Disclosure: [share.gemini.google/US0DiYmqczgg](https://share.gemini.google/US0DiYmqczgg)
