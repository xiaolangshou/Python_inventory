"""webadmins URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from index import views as index_views
from login import views as login_views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^index/', index_views.get_values),
    url(r'^upload/', index_views.upload),
    url(r'^set_cookie/', index_views.set_cookie),
    url(r'^get_cookie/', index_views.get_cookie),
    url(r'^set_session/', index_views.set_session),
    url(r'^get_session/', index_views.get_session),
    url(r'^login/', login_views.login),

]

static_path = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static_path
