"""VenDemo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as login_views
from django.conf.urls.static import static
from django.conf import settings

static_path = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views.login),
    path('cache/', login_views.cache),
    path('home/', login_views.home),
    path('intro/', login_views.intro),
    path('cooper/', login_views.cooper),
    path('about/', login_views.about),
    path('miniProgrammer/', login_views.miniProgrammer),
    path('companyActive/', login_views.companyActive),
    path('tradesActive/', login_views.tradesActive),
    path('developmentActive/', login_views.developmentActive),
    path('e_commerce/', login_views.e_commerce),
    path('website/', login_views.website),
    path('wchat/', login_views.wchat),
    path('business/', login_views.business),
    path('service/', login_views.service),
    path('solution_ecommerce/', login_views.solution_ecommerce),
    path('solution_government/', login_views.solution_government),
    path('solution_company/', login_views.solution_company),
    path('solution_agriculture/', login_views.solution_agriculture)
]

urlpatterns += static_path
