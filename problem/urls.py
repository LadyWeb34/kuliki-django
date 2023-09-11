from django.urls import path
from . import views

urlpatterns = [
    path("problem/", views.problem, name="problem"),
    path('problem/<slug:slug>/', views.detail_page, name='detail_page'),
]