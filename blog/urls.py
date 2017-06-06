from django.conf.urls import url

from blog import views
from blog.views import home, post_detail

urlpatterns = [
    url(r'^$',home, name = "home"),
    url(r'^(?P<id>[0-9])/$', post_detail, name="post"),

]