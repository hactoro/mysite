from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create),
    path('hello', views.hello),
    path('get_note', views.get_note )
]