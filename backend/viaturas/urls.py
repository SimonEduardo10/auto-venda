from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('viaturas/', views.lista_viaturas, name='lista'),

    path('add/', views.adicionar_viatura, name='add'),
    path('edit/<int:id>/', views.editar_viatura, name='edit'),
    path('delete/<int:id>/', views.eliminar_viatura, name='delete'),
]