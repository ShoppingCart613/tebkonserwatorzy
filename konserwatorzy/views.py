from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Zadanie

def index(request):
    zadanie_list = Zadanie.objects.order_by("-data_postu")[:5]
    template = loader.get_template("konserwatorzy/index.html")
    context={"zadanie_list": zadanie_list}
    return HttpResponse(template.render(context,request))

def zadanie(request, zadanie_id):
    zadanie = get_object_or_404(Zadanie, pk=zadanie_id)
    template = loader.get_template("konserwatorzy/zadanie.html")
    context={"zadanie": zadanie}
    return HttpResponse(template.render(context,request))