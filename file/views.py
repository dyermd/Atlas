from django.shortcuts import render, get_object_or_404
from file.models import File
from sample.models import Uses_File
from analysis.models import Analysis

# Create your views here.

#the primary landing page for file
def index(request):
    files = File.objects.all().order_by("name")
    return render(request, 'file/index.html', {'files' : files})

#the detail page of a file
def detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)

    #now we need to grab the list of samples this project uses
    samples = Uses_File.objects.filter(file=file)

    #and now get the analyses
    analyses = Analysis.objects.all()

    return render(request, "file/detail.html", {'file' : file, 'samples' : samples, 'analyses' : analyses})