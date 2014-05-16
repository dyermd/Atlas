from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #p = Paginator(Protein.object.order_by("gene_name"), 10)
    #return send(request, "protein/index.html", {"paginator" : p})
    return render(request, 'protein/index.html')
