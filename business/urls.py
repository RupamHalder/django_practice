from django.urls import path
from .views import *

from . import views

# urlpatterns = [
#     path("", views.about, name="about"),
#     path("", views.services, name="services"),
#     path("", views.portfolio, name="portfolio"),
#     path("", views.contact, name="contact"),
# ]

urlpatterns = [
    path("", HomeView.as_view()),
    path("login/", LoginView.as_view()),
    path("register/", RegisterView.as_view()),
    path("about/", AboutView.as_view()),
    path("services/", ServicesView.as_view()),
    path("portfolio/", PortfolioView.as_view()),
    # path("contact/", ContactView.as_view()),
    path("contact/", views.contact_view, name="contact"),
]