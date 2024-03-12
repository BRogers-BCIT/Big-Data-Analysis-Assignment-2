# pages/urls.py
from django.urls import path
from .views import production_page_view, prediction_page_view, production_post

urlpatterns = [
    path('', production_page_view, name='production'),
    path('productionPost/<type:name>/', production_post, name='productionPost'),
    path('/prediction', prediction_page_view, name='prediction'),
]
