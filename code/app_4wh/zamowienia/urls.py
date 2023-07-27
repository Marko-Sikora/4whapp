from django.urls import path
from . import views

app_name = "zamowienia"
urlpatterns = [
     path('', views.home, name='home'),
    path('detale/', views.lista_detali, name='detale'),
    path("detale/<int:detal_id>/", views.szczegoly_detalu, name="szczegoly"),
    path('detale/zamowienia', views.zamowienia, name='zamowienia'),
    path('popup/', views.popup_view, name='popup_view'),
]