from django.conf.urls import patterns, url

# from printerManager.views import PrinterCommander
from printerManager.views import PrinterCommander
urlpatterns = patterns(
    '', url(
        r'^getCommand/(?P<command_id>\d+)/$',
        PrinterCommander.as_view(),
        name='printerManager'
    ),
)
