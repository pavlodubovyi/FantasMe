from django.shortcuts import render, redirect
from .forms import PlayerCharacterForm


def create_character(request):
    if request.method == 'POST':
        form = PlayerCharacterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerCharacterForm()
    return render(request, 'create_character.html', {'form': form})


def home(request):
    return render(request, 'home.html')