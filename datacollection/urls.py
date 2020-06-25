from django.urls import path

from . import views

app_name = 'datacollection'
urlpatterns = [
    path('', views.enterdata, name="enterdata"),
    path('viewdata/', views.viewdata, name="viewdata"),
]
