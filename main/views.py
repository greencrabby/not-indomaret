from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Not Indomaret',
        'nama': 'Joshua Elisha Shalom Soedarmintarto',
        'kelas': 'PBP E'
    }

    return render(request, "main.html", context)