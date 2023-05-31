from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('search', views.search),
    path('<int:id>', views.post),
    path('create', views.create_view),
    path('success', views.success, name='success'),
]
