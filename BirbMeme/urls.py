from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memes/<int:meme_id>/', views.meme_detail, name='meme_detail'),
    path('creators/<int:creator_id>/', views.creator_detail, name='creator_detail'),
    ]
