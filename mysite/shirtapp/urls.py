from . import views
from django.urls import path

from .views import feedback_view, feedback_list

urlpatterns = [
    path('', views.base, name='base'),
    path('barcelona/', views.tobarcelona, name='tobarcelona'),
    path('real/', views.toreal, name='toreal'),
    path('city/', views.tocity, name='tocity'),
    path('borussiadortmund/', views.todvb, name='todvb'),
    path('united/', views.tountd, name='tountd'),
    path('liverpool/', views.toliverpool, name='toliverpool'),
    path('buy/', views.buy, name='buy'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback_list/', feedback_list, name='feedback_list'),
    path('success/', views.success_page, name='success_page'),
    path('about/', views.about, name='about'),
]
