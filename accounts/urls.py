from django.urls import path
from . import views


app_name='accounts'

urlpatterns = [
    # 유저 목록
    path('', views.index, name='index'),
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
    # 유저 상세보기
    path('<int:user_pk>/', views.detail, name='detail'),
]
