from django.conf.urls import url
from django.conf.urls.static import static

from mysite import settings
from polls import views

urlpatterns = [

    url(r'^$', views.index, name='home'),

    url(r'^(?P<id>[0-9])/$', views.question_details,name="question_detail"),
    url(r'^(?P<id>[0-9])/result/$', views.question_result,name="view_result"),
    url(r'^(?P<id>[0-9])/vote/$', views.question_vote,name= "voting"),


    ]
