from django.conf.urls import include, url
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'dbms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, ),
]