from django.urls import path, re_path
from RCB import views
urlpatterns = [
re_path(r'^$',views.welcome,name = "welcome"),
]