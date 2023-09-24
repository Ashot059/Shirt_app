from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('barcelona/', views.tobarcelona, name='tobarcelona'),
    path('real/', views.toreal, name='toreal'),
    path('city/', views.tocity, name='tocity'),
    path('borussiadortmund/', views.todvb, name='todvb'),
    path('united/', views.tountd, name='tountd'),
    path('liverpool/', views.toliverpool, name='toliverpool'),
]
