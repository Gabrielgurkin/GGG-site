
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index ),
    path('page', views.page ),
    path('loo', views.loo )
]    
