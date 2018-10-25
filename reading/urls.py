from django.urls import path
from . import views

app_name = "reading"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('books/', views.ListsView.as_view(), name="list"),
    path('wisesaying/<int:pk>/', views.WisesayingDetailView.as_view(), name='detail'),
]
