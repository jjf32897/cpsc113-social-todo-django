from django.conf.urls import include, url
from django.contrib import admin

# defines the URL patterns
urlpatterns = [
    url(r'', include('splash.urls')),
    url(r'^task/', include('tasks.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]
