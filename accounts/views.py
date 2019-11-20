from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import *
from .forms import *
# from django.contrib.auth.models import User
# settings.AUTH_USER_MODEL 에 명시된 User 모델을 가져온다.
from django.contrib.auth import get_user_model

User = get_user_model()

# 유저 목록
# AttributeError at /accounts/ 남
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

# 유저 상세보기
def detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)