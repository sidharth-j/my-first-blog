"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from blog.views import home, signup
from mysite import settings
from polls import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^post/$', home,name="home"),
    url(r'^blog/', include('blog.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', signup, name="signup"),
    url(r'^music/', include('music.urls')),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




