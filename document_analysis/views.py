from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pdf2image import convert_from_bytes
from .document.document import DocumentSimilarity
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file_1 = forms.FileField(label="File 1")
    file_2 = forms.FileField(label="File 2")

def index(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print("Reading form")
        if form.is_valid():
            print("Form Valid")
            similarity = get_similarity(request)
            return HttpResponse("The documents are %s similar" % similarity)

    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

def get_similarity(request):
    if len(request.FILES) != 2:
        return HttpResponse("Please upload 2 files", status=400)
    uploaded_file1 = request.FILES["file_1"].read()
    uploaded_file2 = request.FILES["file_2"].read()
    
    image1 = convert_from_bytes(uploaded_file1)
    image2 = convert_from_bytes(uploaded_file2)
    
    doc_sim = DocumentSimilarity()
    
    doc1_text = doc_sim.ocr_conversion(image1[0])
    doc2_text = doc_sim.ocr_conversion(image2[0])

    documents = [doc_sim.preprocess(doc1_text), doc_sim.preprocess(doc2_text)]
    doc_vectors = doc_sim.vectorize(documents)
    similarity_matrix = doc_sim.measure_similarity(doc_vectors)
    return similarity_matrix[0][1]

def result(request, similarity):
    print("Similarity:", similarity)
    return HttpResponse("The documents are %s similar" % similarity)

