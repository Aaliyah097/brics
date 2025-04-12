from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('events/', views.events_view, name='events'),
    path('preferences/', views.preferences_view, name='preferences'),
    path('partners/', views.partners_view, name='partners'),
    path('representatives', views.representatives_view, name='representatives'),
    path('structure/', views.structure_view, name='structure'),
    path('about/', views.about_view, name='about'),
    path('news/', views.news_view, name='news'),
    path('news/<int:news_id>/', views.news_detail_view, name='news_detail'),


]