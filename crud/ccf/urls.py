from django.urls import path
from ccf.views import index

urlpatterns = [
    path('', index),
]
