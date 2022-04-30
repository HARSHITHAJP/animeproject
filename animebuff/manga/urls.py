from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homefunc, name='home_url'),
    
    path('animedetails/',views.animedetailsfunc, name='animedetails_url'),
    path('animewatching/',views.animewatchingfunc, name='animewatching_url'),
    path('blogdetails/',views.blogdetailsfunc, name='blogdetails_url'),
    path('blog/',views.blogfunc, name='blog_url'),

   

    path('login/',views.loginfunc, name='login_url'),

    path('mangaaddform/',views.mangaaddformfunc, name='mangaaddform_url'),

    path('genre/',views.genrefunc, name='genre_url'),
    path('genreaddform/',views.genreaddformfunc, name='genreaddform_url'),
    path('genrelist/',views.genrelistfunc, name='genrelist_url'),


    path('mangalist/',views.mangalistfunc, name='mangalist_url'),
    path('mangareader/',views.mangareaderfunc, name='mangareader_url'),

    path('signup/',views.signupfunc, name='signup_url'),
    
    
]