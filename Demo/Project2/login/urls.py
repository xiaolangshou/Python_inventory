from login import views as login_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', login_views),
]
