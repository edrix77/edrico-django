from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def buku(request):
    # return HttpResponse('Halaman Buku')
    judul = ["belajar django", "belajar python"]
    penulis = "Edrico Alroy"

    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')
