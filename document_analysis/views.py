from django.shortcuts import render
from django.http import HttpResponse
from pdf2image import convert_from_bytes

def index(request):
    if len(request.FILES) != 2:
        return Exception("Need exactly 2 files")
    uploaded_files = request.FILES
    images = convert_from_bytes()
    
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
