from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search'),
    path('search/', views.search_view, name='search'),
    path('bookmarks/', views.bookmark_view, name='bookmarks'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
]