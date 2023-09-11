from django.urls import path
from . import views

urlpatterns = [
    path("people/", views.people, name="people"),
    path('people/<int:pk>/', views.detail_page, name='detail_page'),
]