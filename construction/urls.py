from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('gallery',views.gallery,name='gallery'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('blog',views.blog,name='blog'),
    path('blog/<slug:slug_id>/',views.blogdetail,name='blogdetail'),
    path('ourstory/<slug:slug_id>/',views.ourstorydetail,name='ourstorydetail'),
    path('whatweoffer/<slug:slug_id>/',views.whatweofferdetail,name='whatweofferdetail'),
    path('<int:my_id>',views.aboutusdetail,name='aboutusdetail'),
    path('services/<slug:slug_id>/',views.servicesdetail,name='servicesdetail'),
    path('moreinfo/<slug:slug_id>/',views.moreinfodetail,name='moreinfodetail'),
    path('<int:mm_id>', views.whatwedodetail, name='whatwedodetail'),
    path('contact',views.contact,name='contact'),
]

