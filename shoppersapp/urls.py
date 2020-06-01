from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^mobiles$',views.mobiles_page, name='mobiles_page'),
    url(r'^cars$',views.cars_page,name='cars_page'),
    url(r'^motorcycles$',views.motorcycles_page,name='motorcycles_page'),
    url(r'^laptops$',views.laptops_page,name='laptops_page'),
    #url(r'^blog$',views.blog,name='blog'),



]
