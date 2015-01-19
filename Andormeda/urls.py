from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

CloutPrinterURL = 'cloudPrinter.urls'
PrinterManagerURL = 'printerManager.urls'
Market_URL = 'market.urls'

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', RedirectView.as_view(url='/userRequest/home/')),
    url(r'^userRequest/', include(CloutPrinterURL, namespace="userRequest")),
    # printer/ menas the url about cloud printer. Not the command send to
    # printer or receive information from printer

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^printerRequest/',
        include(PrinterManagerURL, namespace='printerRequest')
        ),

    url(r'^market/', include(Market_URL, namespace='market')),
)
