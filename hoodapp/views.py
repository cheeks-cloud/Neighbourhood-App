from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from .models import Profile,NeighbourHood,Business,Post
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm,HoodForm,BusinessForm,PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    profiles = Profile.objects.filter(id = current_user.id).all()
    hoods = NeighbourHood.objects.all().order_by('-post_date')    
    return render(request, 'index.html',{"profiles": profiles, "hoods":hoods})

@login_required(login_url='/accounts/login/')      
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect ('/index/')
        else:
            form = ProfileForm()
    return render(request, 'update_profile.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})


@login_required(login_url='/accounts/login/')
def createhood(request):
    current_user = request.user
    form = HoodForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request,'create_hood.html',{'form':form})


@login_required(login_url='/accounts/login/')
def neighbourhood(request,id):
    user = request.user
    profiles = Profile.objects.filter(user = user).all()
    businesses = Business.objects.all().filter(neighbourhood_id=id)
    posts = Post.objects.all().order_by('-post_date').filter(neighbourhood_id=id)
    hood = NeighbourHood.objects.get(id=id)
    
    
    
    
    return render(request,'hood.html',{'hood':hood,'posts':posts,'businesses': businesses,'profiles':profiles})

@login_required(login_url='/accounts/login/') 
def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('index')


def change_neighbourhood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/') 
def createbusiness(request, id):
    hood = NeighbourHood.objects.get(id=id)
    current_user = request.user
    form = BusinessForm(request.POST, request.FILES)
    if request.method == 'POST':   
        if form.is_valid():
            bst = form.save(commit=False)
            bst.user = request.user
            bst.neighbourhood = hood
            bst.save()
            return redirect ('neighbourhood', id=hood.id)
        else:
            form = BusinessForm()
    return render(request,'business.html',{'hood':hood, 'form':form})
 

@login_required(login_url='/accounts/login/')
def post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    current_user = request.user
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.neighbourhood = hood
            post.save()
            return redirect ('neighbourhood', hood_id)
        else:
            form = PostForm()
    return render(request,'post.html',{'hood':hood, 'form':form})

@login_required(login_url='/accounts/login/')
def search_results(request):
  if 'business' in request.GET and request.GET["business"]:
    search_term = request.GET.get('business')
    searched_users = Business.search_business(search_term)
    message = f"{search_term}"
    return render(request,'search.html',{"message":message,"results":searched_users})
  else:
    message="You haven't searched for any term."  
    return render(request,'search.html',{"message":message,"results":searched_users})

@login_required(login_url='/accounts/login/')
def search_hoods(request):
    searched_hoods=None
    if 'hoods' in request.GET and request.GET["hoods"]:
        search_term = request.GET.get('hoods')
        searched_hoods = NeighbourHood.search_by_name(search_term)
        message = f"{search_term}"
        return render(request,'search_hood.html',{"message":message,"myhood":searched_hoods})
    else:
    
     message="You haven't searched for any term."  
    return render(request,'search_hood.html', {"message":message, "myhood":searched_hoods})    


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')
