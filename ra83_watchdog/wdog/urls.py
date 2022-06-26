
from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),

    path('post/<slug:worker_id>/', views.post_status, name="post_status"),
]
