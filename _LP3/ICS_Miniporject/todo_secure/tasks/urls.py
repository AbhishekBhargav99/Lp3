from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.showtasks, name='showtasks'),
    path('delete', views.deleteone, name='deleteone'),
    path('complete', views.complete, name='complete'),
    path('deleteall', views.deletealltasks, name='deletealltasks'),
    path('new/', views.addtask, name='addtask'),
]
