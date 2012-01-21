from django.conf.urls.defaults import *
from kanji.models import Kanji

info_dict = {
    'queryset': Kanji.objects.exclude(grade=None),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
)

