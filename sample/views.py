from django.shortcuts import render, get_object_or_404
from sample.models import Sample
from sample.models import Uses_File
from analysis.models import Analysis

# Create your views here.

#the primary landing page for project
def index(request):
    samples = Sample.objects.all().order_by("name")
    return render(request, 'sample/index.html', {'samples' : samples})

#the detail page of a projects
def detail(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)

    #now we need to grab the list of samples this project uses
    files = Uses_File.objects.filter(sample=sample)

    #and now get the analyses
    analyses = Analysis.objects.all()

    return render(request, "sample/detail.html", {'sample' : sample, 'files' : files, 'analyses' : analyses})