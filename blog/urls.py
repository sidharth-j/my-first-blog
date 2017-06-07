from django.conf.urls import url

from blog import views
from blog.views import home, post_detail, add_post, edit_post, delete_post, del_com, signup

urlpatterns = [
    url(r'^$',home, name = "home"),
    url(r'^(?P<id>[0-9]+)/$', post_detail, name="post"),
    url(r'^add/$', add_post, name="add_post"),
    url(r'^(?P<pk>[0-9]+)/edit', edit_post, name="edit_post"),
    url(r'^(?P<id>[0-9]+)/delete', delete_post, name="delete_post"),
    url(r'^(?P<postno>[0-9]+)/delcom/(?P<comno>[0-9]+)', del_com),
    url(r'^accounts/signup/$', signup, name="signup"),


]