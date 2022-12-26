from django.urls import path, include

from .views import index, contacts
from django.conf.urls import handler404, handler500
from core import views

urlpatterns = [
    path('', index),
    path('contacts', contacts),

]

handler404 = views.error404
handler500 = views.error500