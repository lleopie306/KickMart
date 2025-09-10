1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
    Langkah pertama yang aku lakukan saat mengerjakan tugas ini adalah mengikuti seluruh checklist yang sudah diberikan. Setelah itu, aku memikirkan nama yang relevan untuk aplikasi “Football Shop”, lalu memilih nama KickMart.
    
    step yang aku lakukan pertama kali adalah membuat repository baru di GitHub, lalu melakukan clone ke lokal. Aku mengikuti instruksi Tutorial 0 dan Tutorial 1 untuk instalasi Django dan inisiasi proyek Django dan MVT. Di CMD pada direktori kickmart, aku membuat virtual environment dengan:
        python -m venv env
        env\Scripts\activate
    Virtual environment ini berfungsi mengisolasi package dan dependencies agar tidak bentrok dengan versi lain. Aku menyiapkan dependencies dan membuat proyek Django. Di direktori yang sama, aku membuat berkas .txt berisi daftar dependencies, lalu menginstalnya. Setelah itu, aku menjalankan perintah untuk membuat project dan app. Aku melakukan konfigurasi environment variables dan proyek. Environment variables disimpan di luar kode untuk menyimpan informasi konfigurasi seperti kredensial database, API keys, atau pengaturan environment. Aku mengatur settings.py supaya Django “mengerti” struktur proyeknya, lalu menambahkan domain PWS ke ALLOWED_HOSTS (format: <username-sso>-<nama-proyek>.pbp.cs.ui.ac.id). Aku melakukan migrasi database, lalu menjalankan server Django dengan:
        python manage.py runserver
    Jika berhasil, lanjut ke langkah berikutnya.

    Aku melakukan push ke GitHub untuk pekerjaan Instalasi Django dan Inisiasi Proyek Django yang sudah dilakukan. Setelah halaman default Django muncul, aku lanjut ke materi MVT: menjalankan python manage.py startapp main, mendaftarkan 'main' ke INSTALLED_APPS, membuat models sesuai atribut tugas, membuat templates/main.html sederhana (judul KickMart + Name + Class untuk identitas), lalu membuat view show_main yang mengirim context (nama/kelas) ke template. Selanjutnya atur routing: di config/urls.py include main.urls, dan di main/urls.py map "" ke show_main sehingga akses root langsung merender halaman utama. Mengikuti arahan tutorial, aku mendefinisikan model dasar di app (contoh tutorial pakai News, punyaku Product), lalu menjalankan makemigrations dan migrate supaya skema database terbentuk. Terakhir, commit dan push lagi ke GitHub. Kemudian aku Deploy ke PWS: di halaman PWS aku membuat project, menjalankan Project Command yang diberikan PWS (pakai kredensial PWS, bukan SSO). Setelah status berubah dari Building menjadi Running, aku klik View Project saat sudah running.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban :
    ![alt text](<WhatsApp Image 2025-09-10 at 11.21.26_2eb9bce7.jpg>)

3. Jelaskan peran settings.py dalam proyek Django!
Jawaban : 
    menurut aku settings.py itu kayak buku aturan buat proyek Django karena di situ kita ngatur semuanya kaya mau mode belajar atau produksi (DEBUG), kunci rahasia (SECRET_KEY), situs mana yang boleh akses (ALLOWED_HOSTS), aplikasi apa aja yang dipakai (INSTALLED_APPS), jalur halaman & template, sambungan ke database (DATABASES), tempat simpan file statis & media, bahasa dan zona waktu, sampai hal keamanan kayak CSRF. Intinya, supaya si Django tahu “aturan main” proyek kita dari A sampai Z deh.

4. Bagaimana cara kerja migrasi database di Django?
Jawaban : 
    hal pertama yang dilakukan sebelum migrasi data adalah mengubah model (mengedit models.py yang sesuai dengan attribute yang kita mau) kemudian kita lakukan
        python manage.py makemigrations 
    gunanya adalah untuk mencatat setiap perubahan yang ada dan menerapkan ke database yang beneran nya dengan cara  
        python manage.py migrate
    Saat menjalankan makemigrations Django nge-scan models.py buat lihat struktur terbaru terus dibandingin dengan “versi sebelumnya” yang tersimpan di file migrasi. sedangkan kalo menjalankan migrate Django baca semua rencana (file migrasi) dan cek yang belum dijalankan lewat tabel internal. Diurutkan sesuai dependency (biar nggak salah urut antar-app). abis tu diterjemahin jadi perintah SQL sesuai database terus dieksekusi ke database dan dicatat ke django_migrations bahwa migrasinya sudah sukses, jadi nggak dijalankan dua kali.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawaban : 
    menurut aku Django cocok buat mulai karena ia mengajarkan banyak konsep inti rekayasa perangkat lunak secara lengkap buat bikin web. Jadinya kita gak perlu rakit banyak hal sendiri karena udah ada login, database, halaman admin, template, sampai keamanan dasar. Strukturnya juga rapi (model–view–template) jadi kita juga bisa cepat paham sama alurnya. Belajarnya enak karena pakai Python dan cepat lihat hasil (admin langsung jadi). 

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawaban : 
    dari setiap tutorial yang ada sudah cukup baik dan juga sangat detail setiap perintahnya dan apa aja yang udah dikerjain terus dari tutorial itu juga gak cuman sekedar tamplate aja yang kita dapet tapi kita juga jadinya bisa paham setiap penjelasan nya karena beneran di jelasin juga setiap penggunaan nya untuk apa dan buat apa jadinya sejauh ini sudah baik terimakasih ya kak.