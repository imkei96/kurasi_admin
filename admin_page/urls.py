from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.get_list, name='data'),
    path('data/<uid>/', views.get_detail, name='link-uid'),
    path('', include('users.urls')),
]