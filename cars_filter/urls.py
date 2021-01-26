from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cars_filter'

urlpatterns = [
    path('', views.CarsView.as_view(), name='index'),
    # path('search/', views.SearchCarView.as_view(), name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)