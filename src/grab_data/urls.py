from django.conf.urls import url
from . import views

app_name="grab_data"

urlpatterns = [
    url(r'^$', views.Homepage,name="home"),
    url(r'^token/$', views.GetData,name="token"),
    url(r'^instructions/$', views.Instructions,name="instructions"),
    url(r'^about/$', views.About,name="about"),
    url(r'^developer/$', views.Developer,name="developer")
]
