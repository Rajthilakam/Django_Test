from django.conf.urls import url, include
from .import views

app_name = 'testherokuapp'

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^userdetail$', views.results, name='userdetail'),
    url(r'^update_candidateDetail/(\d+)$', views.update_candidatedetail, name = 'update_candidateDetail'),


]