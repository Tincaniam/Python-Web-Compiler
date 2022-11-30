from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('execute_code', views.execute_code, name='index_page')
]