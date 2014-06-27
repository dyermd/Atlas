from django.shortcuts import render, get_object_or_404
from analysis.models import Analysis
from sample.models import Sample
from file.models import File

# Create your views here.
def index(request):
    analyses = Analysis.objects.all().order_by("-date")
    return render(request, 'analysis/index.html', {'analyses' : analyses})

#the detail page of a file
def detail(request, analysis_id):
    analysis = get_object_or_404(Analysis, pk=analysis_id)

    #get the samples
    samples = Sample.objects.all()[:5]

    #get the files
    files = File.objects.all()[:5]

    return render(request, "analysis/detail.html", {'analysis' : analysis, 'samples' : samples, 'files' : files})

def launch(request):
    return render(request, 'analysis/launch.html')

def single_sample_transposon(request):
    files = File.objects.filter(file_type="Transposon Tab")
    return render(request, 'analysis/single_sample_transposon.html', {'files' : files})
