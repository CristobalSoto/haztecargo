from . import views
from django.urls import path, include
urlpatterns = [
    path('deputy/', views.DeputyListCreate.as_view() ),
]