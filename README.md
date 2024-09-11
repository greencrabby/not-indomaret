# not-indomaret

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Membuat sebuah proyek Django baru
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file dengn nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:
`django`
`gunicorn`
`whitenoise`
`psycopg2-binary`
`requests`
`urllib3`
5. Install *dependencies* dengan perintah `pip install -r requirements.txt` dengan virtual environment menyala.
6. Membuat proyek Django dengan nama yang diinginkan melalui perintah `django-admin startproject not-indomaret .`
7. Buka kembali command prompt dan jalankan perintah `python manage.py runserver` dan buka http://localhost:8000 untuk melihat apakah aplikasi Django berhasil dibuat.
8. Hentikan server dengan menekan `Ctrl+C` di command prompt dan jalankan perintah `deactivate` untuk mematikan virtual environment. Push hasil perubahan ke GitHub.

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (windows).
2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama main.
3. Buka berkas settings.py di dalam proyek Django yang dibuat dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
show_main digunakan sebagai tampilan ketika URL yang terkait diakses dan app_name sebagai nama unik pada pola URL aplikasi.
2. Buka berkas `urls.py` di direktori proyek Django dan bukan `urls.py` di direktori `main` dan tambahkan rute URL seperti berikut:
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
`main/` akan diarahkan ke rute yang didefinisikan dalam berkas `urls.py` pada aplikasi `main`.

## Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
1. Buka file `models.py` dan isi file dengan nama dan atribut yang diminta.
2. Berdasarkan ketentuan soal, file minimal harus memiliki isi sebagai berikut:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```
3. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mengaplikasikan perubahan model.

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Buka file `views.py` di dalam direktori `main`.
2. Tambahkan kode berikut ke dalam file.
```python 
from django.shortcuts import render
``` 
3. Tambahkan fungsi berikut ke dalam file.
```python
def show_main(request):
    context = {
        'name': 'nama',
        'class': 'kelas'
    }

    return render(request, "main.html", context)
```
4. Buat direktori dengan nama `templates` di dalam direktori main dan buat file dengan nama `main.html` kemudian isi dengan kode html untuk menampilkan data yang ada di file sebelumnya.
```html
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


## Melakukan deployment ke aplikasi PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buka web PWS dan buat akun melalui akun GitHub. 
2. Setelah login, tekan tombol `Create New Project`.
3. Tambahkan "joshua-elisha-notindomaret.pbp.cs.ui.ac.id" pada `ALLOWEDHOST` .
4. Dalam windows powershell, lakukan `git remote add pws http://pbp.cs.ui.ac.id/joshua.elisha/notindomaret`.
5. Pilih `Pyhon App Template` sebagai *template deployment*.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
`urls.py`:
File ini bertindak sebagai "router" untuk aplikasi. urls.py memetakan pola URL ke fungsi atau kelas tampilan (view) yang sesuai. Ketika pengguna membuat permintaan, Django menggunakan urls.py untuk menentukan tampilan mana yang harus menangani permintaan tersebut.
`views.py`:
Views adalah "pengontrol" dalam pola MVC (Model-View-Controller). View memproses permintaan, berinteraksi dengan model untuk mengambil atau mengubah data, dan menentukan respons apa yang harus dikirim kembali. Jika sebuah view perlu menampilkan data kepada pengguna, biasanya view tersebut akan me-render template HTML.
`models.py`:
Model mendefinisikan struktur data dalam basis data. Model mewakili "lapisan data" dari aplikasi. View berinteraksi dengan model untuk mengambil atau memanipulasi data, dan metode pada model membantu untuk melakukan query pada basis data dengan cara yang lebih abstrak.
`HTML`:
File HTML (atau template) adalah apa yang akhirnya dilihat oleh pengguna. View mengambil data (seringkali dari model) dan me-render-nya ke dalam template HTML, yang kemudian dikirim kembali sebagai respons. Template juga dapat menyertakan konten dinamis dengan menggunakan tag template Django.

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
### Kontrol Versi:
Git melacak perubahan kode sumber seiring waktu. Setiap perubahan dapat "di-commit," menciptakan snapshot proyek pada saat itu, memungkinkan pengembang untuk membandingkan versi dan kembali ke status sebelumnya jika diperlukan.
### Kolaborasi:
Git memungkinkan beberapa pengembang bekerja pada proyek yang sama secara bersamaan dengan menggunakan cabang (branch). Cabang ini bisa digabungkan (merge) saat pekerjaan selesai.
### Branching:
Branching memungkinkan pengembang membuat jalur pengembangan terpisah untuk fitur baru, perbaikan bug, atau eksperimen tanpa mengganggu kode utama. Setelah selesai, cabang ini dapat digabungkan kembali ke cabang utama.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dijadikan framework permulaan dikarenakan Django cukup sederhana sehingga cocok untuk menjadi starting point untuk pembelajaran penggunaan framework

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM karena mereka memungkinkan pengembang untuk bekerja dengan data dari basis data relasional menggunakan objek-objek Python, mengabstraksi detail-detail SQL dan menyediakan cara yang lebih intuitif dan aman untuk mengelola data dalam aplikasi.
