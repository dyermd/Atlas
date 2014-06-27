from django.shortcuts import render, get_object_or_404
from project.models import Project
from project.models import Uses_Sample
from analysis.models import Analysis

# Create your views here.

#the primary landing page for project
def index(request):
    projects = Project.objects.all().order_by("name")
    return render(request, 'project/index.html', {'projects' : projects})

#the detail page of a projects
def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    #now we need to grab the list of samples this project uses
    samples = Uses_Sample.objects.filter(project=project)

    #and now get the analyses
    analyses = Analysis.objects.all()

    return render(request, "project/detail.html", {'project' : project, 'samples' : samples, 'analyses' : analyses})