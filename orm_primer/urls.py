from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sql/", views.sql, name="sql"),
    path("prefetch/", views.prefetch, name="prefetch"),
]
