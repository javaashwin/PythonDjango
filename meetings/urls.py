from django.urls import path

from website import views

from . import views

urlpatterns=[
    path('<int:id>', views.detail,name='detail'),
    path('rooms',views.roomview,name='rooms'),
    path('new',views.new,name='welcome')


]