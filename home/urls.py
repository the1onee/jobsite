
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView

from django.template.defaulttags import url
from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name='home'


urlpatterns = [


    path('',views.viewblog, name='home'),
path('home',views.viewblog, name='home'),

path('portfilo/<slug:slug>/',views.viewportfilo, name='portfilo'),




path('edit/<slug:slug>/', views.viewedit, name='edit'),

path('post/<slug:slug>/', views.viewpostshre, name='post'),
path('catogry/<slug:slug>/', views.viewcatogry, name='catogry'),

    #---------all blog
path('blogperson/<slug:slug>/', views.viewblogforperson, name='person'),
path('blogcom/<slug:slug>/', views.viewblogforcomp, name='person'),

    #----------read plog
path('readblog/<slug:slug>/', views.viewblogread, name='readblog'),
path('readblogcom/<slug:slug>/', views.viewblogreadcom, name='readblogcom'),

#----------404


    #--------------porfilo
path('portfilo/<slug:slug>/',views.viewportfilo, name='portfilo'),


    #------ index
path('index/<slug:slug>/',views.viewindex, name='index'),
path('indexcom/<slug:slug>/',views.viewindexcom, name='indexcom'),


#===sin in
path('sinupcom/', views.signup_com, name='signupcom'),
path('sinup/', views.signup, name='signup'),
path('login/',views.login_request, name='login'),
path('logout/', LogoutView.as_view(next_page='http://127.0.0.1:8000/home'), name='logout'),

]

