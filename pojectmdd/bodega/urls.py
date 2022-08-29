from django.urls import path
from . import views
from django.urls.conf import include
from django.conf import settings


urlpatterns = [
    path('', views.home, name='index'),
    path('bodeguero/', views.bodeguero, name="bodeguero"),
    path('elementos/', views.elementos, name="elementos"),
    path('bodegas/', views.bodegas, name="bodegas"),
    path('bodegas/<int:id>', views.bodegas_id, name="bodegas"),
    path('delegaciones/', views.delegaciones, name="delegaciones"),
    path('update_bodega/<int:bodegas>', views.update_bodega, name="update_bodega"),
    path('delete_bodega/<int:bodegas>', views.delete_bodega, name="delete_bodega")
]