from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact_form", views.contact_form, name="contact_form"),
    path("contact_form/complete", views.complete, name="complete"),
]
