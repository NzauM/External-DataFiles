from unicodedata import name
from django.urls import path
from .import views

urlpatterns=[
    path("",views.listUsers, name="listusers"),
    path("showguest/<int:id>",views.getGuest, name="showguest" ),
    path("newguest", views.guestForm, name="guestForm"),
    path("updateguest/<int:id>", views.updateGuest, name="updateguest"),
    path("deleteguest/<int:id>", views.deleteGuest, name="deleteguest")

]