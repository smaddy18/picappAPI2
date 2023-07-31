from django.urls import path
from . import views

urlpatterns = [
    #path('', views.list, 'roompic-list'),
    path('upload/', views.upload, name='roompic-upload')
]
