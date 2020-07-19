from django.shortcuts import render
from .models import Proyect

# Create your views here.
def portfolio(request):
    projects = Proyect.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects' : projects})