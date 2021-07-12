from django.urls import path
from .views import *

urlpatterns=[
    path('',home_page, name="home_page"),
    path('login/',login_page, name="login_page"),
    path('logout/',logout_page, name="logout_page"),

    path('auhtor/list/',author_list, name="author_list"),
    path('author/create/',author_create, name="author_create"),
    path('author/<int:pk>/edit/', author_edit, name = 'author_edit'),
    path('author/<int:pk>/delete/', author_delete, name = 'author_delete'),

    path('category/list/', category_list, name="category_list"),
    path('category/create/', category_create, name="category_create"),
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),

    path('book/list/', book_list, name="book_list"),
    path('book/create/', book_create, name="book_create"),
    path('book/<int:pk>/edit/', book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),

]