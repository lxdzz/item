from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('logout/', logout),

]