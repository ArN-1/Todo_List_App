# Studi Kasus Aplikasi Todo List:


<details>
<summary> Fitur -Fitur</summary>

- Autentikasi pengguna (login dan register)
- Penambahan, pengeditan, dan penghapusan todo
- Pencarian todo berdasarkan kategori
- Penandai todo sebagai selesai atau belum selesai
- Penambahan kategori todo
- Pencarian todo berdasarkan tanggal
- Notifikasi email saat todo mendekati batas waktu

</details>

<details>
<summary> Stack Teknologi </summary>

- Backend: Python dengan framework Flask dan database MySQL
- Frontend: HTML, CSS (menggunakan framework Tailwind) dan JavaScript (menggunakan framework Vue.js)
</details>
<details>
<summary> Arsitektur</summary>

- Penggunaan REST API untuk komunikasi antara backend dan frontend
- Penggunaan JWT untuk autentikasi dan validasi token
- Penyimpanan data todo dan kategori todo dalam database MySQL
</details>
<details>
<summary>Alur aplikasi</summary>

- Pengguna melakukan registrasi atau login
- Pengguna dapat menambah, mengedit, dan menghapus todo sesuai dengan kategori yang telah ditentukan
- Pengguna dapat menandai todo sebagai selesai atau belum selesai
- Pengguna dapat menambah kategori todo
- Pengguna dapat mencari todo berdasarkan tanggal dan kategori
- Pengguna akan menerima notifikasi email saat todo mendekati batas waktu
</details>

<details>
<summary>Keuntungan Aplikasi</summary>

- Membantu pengguna untuk mengelola todo dengan lebih efisien dan efektif
- Pengguna dapat mengatur todo sesuai dengan kategori yang telah ditentukan
- Pengguna dapat menandai todo sebagai selesai atau belum selesai
- Pengguna dapat menambah kategori todo
- Pengguna dapat mencari todo berdasarkan tanggal dan kategori
- Pengguna akan menerima notifikasi email saat todo mendekati batas waktu
</details>

<details>
<summary>Struktur direktori </summary>

##  |-- backend/
- |   |-- app.py
- |   |-- config.py
- |   |-- database.py
- |   |-- models.py
- |   |-- controllers/
- |       |-- todo_controller.py
## |-- frontend/
- |   |-- index.html
- |   |-- css/
- |   |   |-- tailwind.css
- |   |-- js/
- |       |-- main.js


</details>