from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def create_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user
            neighbourhood.save()
            messages.success(
                request, 'You have succesfully created a Neighbourhood.')
            return redirect('neighbourhood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'new_hood.html', {'form': form})