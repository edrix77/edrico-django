from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def buku(request):
    return HttpResponse('Halaman Buku')
def penerbit(request):
    return HttpResponse('Halaman Penerbit')
