from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.index, name='landing'),
    url(r'^upload/$', views.new_project, name='newPro'),


    

]
