
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index ),
    path('page', views.page, name='home' ),
    path('page0', views.page0, name='page0' ),
    path('page1', views.page1, name='page`' ),
    path('page2', views.page2, name='page2' ),
    path('page3', views.page3, name='page3' ),
    path('page4', views.page4, name='page4' ),
    path('page5', views.page5, name='page5' ),
    path('page6', views.page6, name='page6' ),
    path('page7', views.page7, name='page7' ),
    path('page8', views.page8, name='page8' ),
    path('page9', views.page9, name='page9' ),
    path('page10', views.page10, name='page10' ),
    path('page11', views.page11, name='page11' ),
    path('page12', views.page12, name='page12' ),
    path('page13', views.page13, name='page13' ),
    path('politicconf', views.politicconf, name='politicconf' ),
    

]    
