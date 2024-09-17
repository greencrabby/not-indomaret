# not-indomaret

# ---TUGAS 2---

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat sebuah proyek Django baru
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file dengan nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:
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

### Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (windows).
2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama main.
3. Buka file `settings.py` di dalam proyek Django yang dibuat dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuat file dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
show_main digunakan sebagai tampilan ketika URL yang terkait diakses dan app_name sebagai nama unik pada pola URL aplikasi.
2. Buka file `urls.py` di direktori proyek Django dan bukan `urls.py` di direktori `main` dan tambahkan rute URL seperti berikut:
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
`main/` akan diarahkan ke rute yang didefinisikan dalam file `urls.py` pada aplikasi `main`.

### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
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

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Membuat file dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


### Melakukan deployment ke aplikasi PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buka web PWS dan buat akun melalui akun GitHub. 
2. Setelah login, tekan tombol `Create New Project`.
3. Tambahkan "joshua-elisha-notindomaret.pbp.cs.ui.ac.id" pada `ALLOWEDHOST` .
4. Dalam windows powershell, lakukan `git remote add pws http://pbp.cs.ui.ac.id/joshua.elisha/notindomaret`.
5. Pilih `Pyhon App Template` sebagai *template deployment*.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img src="readmeassets/diagram.png">

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

# ---TUGAS 3---

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam implementasi platform untuk memastikan komunikasi yang efisien antar komponen, dengan transfer data yang tepat waktu dan sinkronisasi. Hal ini membuat data delivery lebih time efficient dan juga tentunya setiap komponen dapat sinkron. Kemudian data delivery juga memastikan integritas data sehingga memungkinkan platform untuk berkembang tanpa mengorbankan kinerja.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dikarenakan data yang ditampilkan lebih mudah untuk dipahami dibandingkand engan format XML. JSON lebih populer daripada XML karena lebih sederhana, ringkas, dan mudah dipahami. Parsing JSON lebih cepat dan efisien, dengan ukuran data yang lebih kecil, serta dukungan luas di berbagai bahasa pemrograman. Ini membuat JSON lebih cocok untuk aplikasi web dan API modern.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() memastikan input yang diberikan valid, dengan cara periksa input setelah form ter-submit. Hal ini dibutuhkan karena data yang di-input harus dipastikan sudah benar, sehingga memiliki efek samping seperti memberi proteksi terhadap SQL injection sehingga dipastikan bahwa input adalah yang diinginkan.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Dalam Django, csrf_token penting untuk melindungi form dari serangan Cross-Site Request Forgery (CSRF). Tanpanya, penyerang bisa memanipulasi pengguna untuk mengirim form tanpa disadari, memungkinkan tindakan tidak sah seperti perubahan data atau pembelian. Token ini memastikan form dikirim dari sumber yang tepercaya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Membuat direktori baru `templates` dengan file `base.html` dengan isi berikut:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
2. Buka file `settings.py` dalam direktori `not_indomaret` kemudian menambahkan kode berikut:
```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
...
```
3. Buka file `models.py` dalam direktori `main` kemudian menambahkan kode berikut:
```python
import uuid  # tambahkan baris ini di paling atas
...
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
...
```
Lalu juga melakukan migrasi model dengan cara
```
python manage.py makemigrations
python manage.py migrate
```
4. Membuat file `forms.py` dalam direktori `main` dan diisi dengan kode berikut:
```python
from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]
```
5. Buka file `views.py` dalam direktori `main` kemudian menambahkan kode berikut:
```python
from django.shortcuts import render, redirect 
from main.forms import ProductEntryForm
from main.models import ProductEntry

...
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
Juga update fungsi `show_main` menjadi seperti berikut:
```python
def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'app_name' : 'Not Indomaret',
        'npm': '2306275001',
        'name': 'Joshua Elisha Shalom Soedarmintarto',
        'class': 'PBP E',
        'product_entries': product_entries,
    }

    return render(request, "main.html", context)
```
6. Buka file `urls.py` dalam direktori `main` kemudian menambahkan kode berikut:
```python
from django.urls import path
from main.views import show_main, create_product_entry

urlpatterns = [
   ...
    path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```
7. Buat file `create_product_entry.html` dalam direktori `main/templates` dengan isi kode:
```python
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Mood Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
8. Buka file `main.html` dalam direktori `main/templates` kemudian menambahkan kode berikut:
```html
...
{% if not product_entries %}
<p>Belum ada data product pada {{app_name}}.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
  </tr>

  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```

### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Buka file `views.py` dalam direktori `main` kemudian tambahkan kode berikut:
```py
...
from django.http import HttpResponse
from django.core import serializers
...

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Buka file `urls.py` dalam direktori `main` kemudian tambahkan kode berikut:
```python
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. XML view
<img src="readmeassets/xml_view.png">
2. JSON view
<img src="readmeassets/json_view.png">
3. XML ID view
<img src="readmeassets/xml_id_view.png">
4. JSON ID view
<img src="readmeassets/json_id_view.png">