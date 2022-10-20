from os import path

from math_app import views

urlpatterns = [
    path('', views.MathService, name='home'),
]
