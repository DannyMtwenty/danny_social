
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('settings', views.settings, name='settings'),
    path('logout', views.logout, name='logout'),
    path('like-post', views.like_post, name='like-post'),
    path('upload', views.upload, name='upload'),

]
