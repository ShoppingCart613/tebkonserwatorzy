from django.shortcuts import get_object_or_404, render, redirect
from .models import Zadanie
from .forms import ZadanieForm, LoginForm, ZadanieEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logouts

#logowanie
def form_login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    return render(request, 'konserwatorzy/login.html', {'form': form})

def logout(request):

    logouts(request)
    return redirect('login')

#zadania
@login_required
def index(request):
    zadanie_list = Zadanie.objects.order_by('-data_postu')

    return render(request, 'konserwatorzy/index.html',{"zadanie_list": zadanie_list})

@login_required
def zadanie(request, zadanie_id):
    zadanie = get_object_or_404(Zadanie, pk=zadanie_id)
    return render(request,"konserwatorzy/zadanie.html",{"zadanie": zadanie})

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

@login_required
def edit(request, zadanie_id):
    zadanie = get_object_or_404(Zadanie, pk=zadanie_id)
    if request.method == "POST":
        zadanie_form = ZadanieForm(request.POST)
        if zadanie_form.is_valid():
            new_zad = zadanie_form.save(commit=False)
            new_zad.save()
        return render(request, 'konserwatorzy/zadanie.html',{'zadanie':new_zad})
    else:
        zadanie_form = ZadanieEditForm(instance=zadanie)
    
    return render(request, 'konserwatorzy/edit.html', {'zadanie_form':zadanie_form})