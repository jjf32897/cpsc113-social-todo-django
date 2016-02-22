from django.conf.urls import url

from . import views

# routes to the user functions
urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^logout', views.logout, name='logout')
]
