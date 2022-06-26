
from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('worker/', views.work, name="work"),
    path('req/', views.req, name="req")
]
