from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.get_list, name='data'),
    path('data/<uid>/', views.get_detail, name='link-uid'),
    path('', include('users.urls')),
    path('accept/<uid>', views.accept, name='accept'),
    path('data_curated/', views.curated_list, name='data_curated'),
    path('data_curated/<uid>', views.curated_detail, name='uid-curated'),

]