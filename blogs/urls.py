from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('blogs', views.index, name='blogs' ),
    path('eachblog', views.userBlogs, name='eachblog'),
    path('addBlog',views.createNew, name='addBlog')
]
