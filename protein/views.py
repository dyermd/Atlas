from django.shortcuts import render
from django.http import HttpResponse
from protein.models import Protein
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #p = Paginator(Protein.object.order_by("gene_name"), 10)
    #return send(request, "protein/index.html", {"paginator" : p})
    first_five_proteins = Protein.objects.order_by('-gene_name')[:5]
    context = {'first_five_proteins' : first_five_proteins}
    return render(request, 'protein/index.html', context)
