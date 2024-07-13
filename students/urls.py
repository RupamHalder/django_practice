from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-two-values/", views.add_two_values, name="add_two_values"),
    path("addition-result/", views.addition_result, name="addition_result"),
]