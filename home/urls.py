from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('about',about,name="about"),
    path('blog-home',bloghome,name="blog-home"),
    path('blog-single',blogsingle,name="blog-single"),
    path('contact',contact,name="contact"),
    path('elements',elements,name="elements"),
    path('portfolio',portfolio,name="portfolio"),
    path('price',price,name="price"),
    path('services',services,name="services"),
]




