from django.conf.urls import patterns, url

from cloudPrinter import views
from cloudPrinter.views import UploadHolder
from cloudPrinter.views import SubmitHandler
from cloudPrinter.views import SucceedView
from cloudPrinter.views import TestPer

urlpatterns = patterns(
    '', url(r'^upload/$', views.upload, name='uploadFiles'),
    url(r'^home/$', views.index, name='index'),
    url(r'^configure/$', UploadHolder.as_view(), name='configure'),
    url(r'^submit/$', SucceedView.as_view(), name='submitJob'),
    url(r'^testPer/$', TestPer.as_view(), name='testPer'),
    url(r'^startPrinting/$', SubmitHandler.as_view(), name='startPrinting'),
)
