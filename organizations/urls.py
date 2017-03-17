from django.conf.urls import url

from . import views

app_name = "organizations"
urlpatterns = [
  url(r'^$', views.list, name="list"),
  url(r'^(?P<pk>\d+)/$', views.detail, name="detail")
]
