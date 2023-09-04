from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('filter/<str:order_by>/', views.order_filter, name='filter'),
    path('emph/<int:person_id>/', views.emphasis, name='emphasis'),
    path('del/<int:person_id>/', views.delete, name='delete'),
    path('up_name/<int:person_id>/', views.up_name, name='up_name'),
    path('up_birth/<int:person_id>/', views.up_birth, name='up_birth'),
    path('up_photo/<int:person_id>/', views.up_photo, name='up_photo')
]
