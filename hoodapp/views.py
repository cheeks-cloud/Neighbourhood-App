from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def businesses(request,id):
    business = Business.hoods_business(id=id)
    return render(request, 'business.html',{'business':business})
    
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user

            business.save()

        return redirect('business')

    else:
        form = BusinessForm()
    return render(request, 'new_business.html', {"form": form})

def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()
            messages.success(request, 'You have succesfully created a Post')

        return redirect('post')

    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})
