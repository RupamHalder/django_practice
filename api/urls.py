from django.urls import path

from . import views

urlpatterns = [
    path("student/view", views.get_all_students),
    path("student/add", views.add_student),
]