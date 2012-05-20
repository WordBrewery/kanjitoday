from django.conf.urls.defaults import *
from feeds import KanjiOfTheDayFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'kanji.views.frontpage'),
#    (r'^kanji/', include('kanji.urls')),
    (r'^feed/$', KanjiOfTheDayFeed()),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
