from django.conf.urls import url
from binApp import views


urlpatterns = [
	url(r'get_freq', views.binApi),
]
