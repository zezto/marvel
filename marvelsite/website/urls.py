from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    re_path(r'^(?P<article_id>[0-9]+)$', views.detail, name='details'),
    path('comments', views.comments, name='comments')

]