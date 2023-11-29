from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("home/homeuser/index/", login_required(views.index), name="index"),
    path("home/homeuser/index/lugares/<str:lugar>", login_required(views.S2ndView), name="S2ndView"),
    path('home/homeuser/formulario/', login_required(views.mostrar_formulario), name='mostrar_formulario'),
    path('guardar_lugar/', login_required(views.guardar_lugar), name='guardar_lugar'),  # Vista protegida por login_required
    path('home/', views.home, name='inicio'),
    path('home/homeuser/index/paginadeayuda.html',login_required(views.ayuda), name='ayuda'),
    path('home/login', LoginView.as_view(template_name='formulariologuin.html'), name='login'),
    path('home/registro', views.registro_view, name='registro'),
    path('favorito/<int:lugar_id>/', login_required(views.favoritos), name='toggle_favorito'),  # Vista protegida por login_required
    path('home/homeuser/favoritos/', login_required(views.favoritos), name='favoritos'),
    path('home/homeuser/', login_required(views.homeuser), name='homeuser'),
    path('', LogoutView.as_view(), name='logout')
    
]
