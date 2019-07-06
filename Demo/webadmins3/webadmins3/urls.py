"""webadmins3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from login import views as login_views

from django.conf.urls.static import static
from django.conf import settings

static_path = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_views.login),
    url(r'^upload/', login_views.file_upload),
    url(r'^cache/', login_views.cache),
    url(r'^setcookie/', login_views.setCookies),
    url(r'^getcookie/', login_views.getCookies),
    url(r'^login/', login_views.login),
    url(r'^index/', login_views.index),
    url(r'^logout/', login_views.logout),
    url(r'^home/', login_views.home),
]

urlpatterns += static_path
