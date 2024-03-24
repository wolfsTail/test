from django.urls import path

from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='list'),
    path('results/<int:file_id>/', views.get_result, name='detail'),
]
