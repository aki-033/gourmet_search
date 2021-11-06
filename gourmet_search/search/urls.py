from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index_page),
    path('<str:middle>/', views.small_area, name='small'),
    path('<str:middle>/<str:small>', views.genre, name='genre'),
    path('<str:middle>/<str:small>/<str:genre>', views.shop, name='shop'),
]
