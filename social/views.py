from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from social.models import Post
from .models import *
from .forms import UserRegisterForm,PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def feed(request):
    posts= Post.objects.all()
    context={'posts':posts}
    return render(request,'social/feed.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #para guardar el registro en la 
            form.save()
            username= form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('feed')
    else:
        print("no registrado")
        form =UserRegisterForm()
    context ={'form':form}
    return render(request,'social/register.html',context)
# estas funciones solo se puede realizar si se esta logueado
@login_required
def post(request):
    #obtengo el usuario que esta logeado dentro de la app
    current_user= get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
          post=  form.save(commit=False)
          post.usuario = current_user
          post.save()
          messages.success(request,'Post enviado')
          return redirect('feed')
    else:
        form=PostForm()
    return render(request,'social/post.html',{'form':form})


def profile(request,username=None):
    #obtengo el usuario que esta logeado dentro de la app
    current_user=request.user
    if username and username != current_user.username:
        #BUSCAR  USUARIO DE LA BASE DE DATOS 
        user = User.objects.get(username= username)

        posts=user.posts.all()
    else :
        posts=current_user.posts.all()
        user =current_user
    return render(request,'social/profile.html',{'user':user, 'posts':posts})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')

def misFollow(request):
    seguidores= Relationship.objects.all()
    context={'seguidores':seguidores}
    return render(request,'social/seguidores.html',context)