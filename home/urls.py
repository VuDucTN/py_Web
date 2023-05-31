from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.index,),
    path('contact/', views.contact,),
    path('about/', views.about),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', views.profile, name='users-profile'),
]
