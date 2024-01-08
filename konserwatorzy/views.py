from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from .models import Zadanie
from .forms import ZadanieForm, LoginForm
from django.contrib.auth.decorators import login_required

#logowanie
def form_login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    return render(request, 'konserwatorzy/login.html', {'form': form})

#zadania
@login_required
def index(request):
    zadanie_list = Zadanie.objects.order_by("-data_postu")[:5]
    template = loader.get_template("konserwatorzy/index.html")
    context={"zadanie_list": zadanie_list}
    return HttpResponse(template.render(context,request))

@login_required
def zadanie(request, zadanie_id):
    zadanie = get_object_or_404(Zadanie, pk=zadanie_id)
    template = loader.get_template("konserwatorzy/zadanie.html")
    context={"zadanie": zadanie}
    return HttpResponse(template.render(context,request))

@login_required
def add_zadanie(request):
    if request.method == 'POST':
        zadanie_form = ZadanieForm(request.POST)
        if zadanie_form.is_valid():
            new_zad = zadanie_form.save(commit=False)
            new_zad.save()
        return render(request, 'konserwatorzy/dodano.html')

    else:
        zadanie_form = ZadanieForm()
    return render(request, 'konserwatorzy/dodaj_zadanie.html',{'zadanie_form': zadanie_form})