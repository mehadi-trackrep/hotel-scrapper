from django.urls import path
from . import views
from .views import CustomLoginView, register_view, logout_any

urlpatterns = [
    path('', views.search_view, name='search'),
    path('search/', views.search_view, name='search'),
    path('bookmarks/', views.bookmark_view, name='bookmarks'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('remove_bookmark/<int:pk>/', views.remove_bookmark, name='remove_bookmark'),
    path('logout/', logout_any, name='logout'),

]